from MyDjangoNFT.views import LeadListCreate
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path, include
from . import views
from .sitemaps import LeadSitemap, StaticSitemap
from django.views.generic.base import TemplateView

app_name = 'main'


sitemaps = {
    'leads':LeadSitemap,
    'static':StaticSitemap,
}

# здесь не будет работать с шаблонами
urlpatterns = [
    path('', views.home),
    
]







