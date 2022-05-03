=====
My Pet Project
=====
This project show how will show the portfolio-site look like on real hosting server.
Detailed documentation in the "doc" directory.

1. Add "MainSite" to your INSTALLED_APPS settings like this:
   
    INSTALLED_APPS = [
        ...
        'MainSite.apps.MainsiteConfig',
    ]

2. Include the MainSite in your project urls.py like this:

    path('mainsite/', include('MainSite.urls'))

3. Run "python manage.py migrate" to create the MainSite models.

4. Start the development localhost server and visit:
    http://127.0.0.1:8000/admin/
    to create a MainSite (you'l need the admin app enabled).

5. Visit the http://127.0.0.1:8000/mainsite/ to enteract with the MainSite app.












