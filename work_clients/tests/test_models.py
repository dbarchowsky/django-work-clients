from django.test import TestCase
from work_clients.models import Client, Industry


class ClientTestCase(TestCase):
    def test_client_is_design_related(self):
        """Clients are correctly identified as being design related."""

        i = Industry(name="Animation")
        i.save()
        c = Client(name="My Animation Client")
        c.save()
        c.industries.add(i)
        self.assertTrue(c.is_design_related(), "Client is correctly identified as design related.")

    def test_client_is_not_design_related(self):
        """Clients are correctly identified as being not design related."""

        i = Industry(name="Web Development")
        i.save()
        c = Client(name="My Web Client")
        c.save()
        c.industries.add(i)
        self.assertFalse(c.is_design_related(), "Client is correctly identified as not design related.")
