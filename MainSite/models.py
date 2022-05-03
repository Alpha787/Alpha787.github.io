from django.db import models
from django.core.mail import EmailMessage, get_connection, send_mail


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

# class Article(models.Model):
#     pass




