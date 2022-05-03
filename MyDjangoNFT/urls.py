from django.contrib import admin
from django.urls import path, include
import MainSite.views as views

# модернезированные URL проекта
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('MainSite.urls')),

    path('', views.home, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact-form', views.contact, name='contact'),
    # path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('work', views.work, name='work'),
    path('work-single', views.work_single, name='work-single'),
    path('404', views.error_404, name='error_404'),
]
