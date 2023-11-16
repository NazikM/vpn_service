from django.db import models

from vpn_service.models import Site


class VPNStatistic(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    transitions = models.PositiveIntegerField(default=0)
    uploaded_data = models.PositiveIntegerField(default=0)
    downloaded_data = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.site.name + " stats"
