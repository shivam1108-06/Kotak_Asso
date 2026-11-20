import re

from django.conf import settings

_GA_ID = re.compile(r"^G-[A-Z0-9]{4,20}$")

_SOCIAL_META = [
    ("linkedin", "LinkedIn", "fab fa-linkedin-in"),
    ("x_twitter", "X (Twitter)", "fab fa-x-twitter"),
    ("facebook", "Facebook", "fab fa-facebook-f"),
    ("instagram", "Instagram", "fab fa-instagram"),
]


def site_info(request):
    """Values every template needs: social profiles that have a URL set, and
    the client portal link."""
    links = getattr(settings, "SOCIAL_LINKS", {})
    social_links = [
        {"name": name, "icon": icon, "url": links[key]}
        for key, name, icon in _SOCIAL_META
        if links.get(key)
    ]
    return {
        "social_links": social_links,
        "client_portal_url": getattr(settings, "CLIENT_PORTAL_URL", ""),
        "ga_measurement_id": _ga_id(),
    }


def _ga_id():
    # Only accept a real-looking GA4 ID, so a typo can't break the page.
    value = getattr(settings, "GA_MEASUREMENT_ID", "").upper()
    return value if _GA_ID.match(value) else ""
