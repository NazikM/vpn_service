from django.db import models
from django.contrib.auth.models import User


class Site(models.Model):
    """
    Структура сайту.

    URL: URL-адреса сайту.
    Name: Назва сайту.
    """

    url = models.URLField(verbose_name="URL")
    name = models.CharField(max_length=255, verbose_name="Site name")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name