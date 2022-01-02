from django.urls import path
from .views import index, about, blog, contact, services, work, work_single, error_404
from MyDjangoNFT.views import LeadListCreate
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', index, name='homepage'),
    # path('admin/', admin.site.urls),
    path('index.html', index, name='home_view'),
    path('about.html', about, name='about'),
    path('blog.html', blog, name='blog'),
    path('contact.html', contact, name='contact'),
    path('services.html', services, name='services'),
    path('work.html', work, name='work'),
    path('work-single.html', work_single, name='work_single'),
    path('404.html', error_404, name='error_404'),

]







