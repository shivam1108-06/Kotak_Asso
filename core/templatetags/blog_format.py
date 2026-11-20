"""Turns the plain text of a blog post into simple, safe HTML.

Rules (also shown as help text in the admin):
  * blank line            -> new paragraph
  * "## Heading"          -> sub-heading   ("### " for a smaller one)
  * "- item" / "* item"   -> bullet list
  * "1. item"             -> numbered list
  * **bold**              -> bold text
  * web addresses         -> links

Everything is HTML-escaped first, so nothing typed in the admin can inject
markup or scripts into the page.
"""
import re

from django import template
from django.utils.html import escape, urlize
from django.utils.safestring import mark_safe

register = template.Library()

_BULLET = re.compile(r'^[-*•]\s+(.*)$')
_NUMBERED = re.compile(r'^\d+[.)]\s+(.*)$')
_BOLD = re.compile(r'\*\*(.+?)\*\*')


def _inline(text):
    # urlize() escapes its input itself, so pass raw text then add bold.
    html = urlize(text, nofollow=False, autoescape=True)
    html = html.replace('<a ', '<a target="_blank" rel="nofollow noopener" ')
    return _BOLD.sub(r'<strong>\1</strong>', html)


@register.filter
def render_body(text):
    out, para, list_tag, items = [], [], None, []

    def flush_para():
        if para:
            out.append('<p>' + '<br>'.join(_inline(l) for l in para) + '</p>')
            para.clear()

    def flush_list():
        nonlocal list_tag
        if list_tag:
            out.append(f'<{list_tag}>' + ''.join(f'<li>{_inline(i)}</li>' for i in items) + f'</{list_tag}>')
            items.clear()
            list_tag = None

    for raw in (text or '').replace('\r\n', '\n').split('\n'):
        line = raw.strip()
        if not line:
            flush_para(); flush_list()
            continue
        if line.startswith('### ') or line.startswith('## '):
            flush_para(); flush_list()
            tag = 'h3' if line.startswith('### ') else 'h2'
            out.append(f'<{tag}>{escape(line.lstrip("#").strip())}</{tag}>')
            continue
        bullet, numbered = _BULLET.match(line), _NUMBERED.match(line)
        if bullet or numbered:
            flush_para()
            tag = 'ul' if bullet else 'ol'
            if list_tag and list_tag != tag:
                flush_list()
            list_tag = tag
            items.append((bullet or numbered).group(1))
            continue
        flush_list()
        para.append(line)

    flush_para(); flush_list()
    return mark_safe('\n'.join(out))
