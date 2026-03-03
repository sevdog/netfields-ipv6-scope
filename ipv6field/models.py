from django.db import models
from netfields import InetAddressField


class IpModel(models.Model):
    ip = InetAddressField(null=True, blank=True)
    dj_ip = models.GenericIPAddressField(null=True, blank=True)