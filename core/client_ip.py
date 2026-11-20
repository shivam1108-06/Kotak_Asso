"""Find the visitor's real IP address, in a way visitors cannot fake.

On Railway every request passes through Railway's proxy, which adds the
visitor's address to the end of the X-Forwarded-For header. Anything earlier
in that header was sent by the visitor and could be made up, so we count
TRUSTED_PROXY_COUNT entries from the *right*.

TRUSTED_PROXY_COUNT is 1 on Railway. If Cloudflare is put in front of the site
(two proxies), set it to 2. Locally it is 0, so REMOTE_ADDR is used.

Used by the admin login lockout (django-axes) and the form spam limits.
"""
from django.conf import settings


def get_client_ip(request):
    proxies = getattr(settings, 'TRUSTED_PROXY_COUNT', 0)
    if proxies > 0:
        forwarded = request.META.get('HTTP_X_FORWARDED_FOR', '')
        parts = [p.strip() for p in forwarded.split(',') if p.strip()]
        if len(parts) >= proxies:
            return parts[-proxies]
    return request.META.get('REMOTE_ADDR', '')
