from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import BlogPost
from .views import SERVICES_DATA


class StaticPagesSitemap(Sitemap):
    changefreq = 'monthly'

    def items(self):
        return ['home', 'about', 'services', 'benefits', 'process', 'gallery',
                'team', 'testimonials', 'contact', 'blog_list',
                'privacy_policy', 'terms_of_service']

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return 1.0 if item == 'home' else 0.7


class ServicesSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return list(SERVICES_DATA.keys())

    def location(self, slug):
        return reverse('service_detail', args=[slug])


class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return BlogPost.live()

    def lastmod(self, post):
        return post.updated_at


SITEMAPS = {
    'pages': StaticPagesSitemap,
    'services': ServicesSitemap,
    'blog': BlogSitemap,
}
