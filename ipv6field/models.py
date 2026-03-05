from django.db import models
from netfields import InetAddressField


class IpModel(models.Model):
    ip = InetAddressField(null=True, blank=True)
    ip_no_prefix = InetAddressField(null=True, blank=True, store_prefix_length=False)
    dj_ip = models.GenericIPAddressField(null=True, blank=True)