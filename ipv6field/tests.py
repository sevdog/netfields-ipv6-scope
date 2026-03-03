from django.test import TestCase
from .models import IpModel


class IPv6ScopeTestCase(TestCase):

    def test_ipv6_scope_ip_parsing_netfield(self):
        elem = IpModel.objects.create(ip='2001:db8::1%foo')

    def test_ipv6_scope_ip_parsing_django(self):
        elem = IpModel.objects.create(dj_ip='2001:db8::1%foo')