from django.contrib.sitemaps import Sitemap
from .models import Lead
from django.urls import reverse

# TODO: доделать sitemap
class LeadSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'http'

    def items(self):
        return Lead.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return f'/blog/{obj.article_slug}' 

class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['main:homepage_view', 'main:contact_view']
    
    def location(self, item):
        return reverse(item)
















