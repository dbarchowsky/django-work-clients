from django.db import models
from django.core import urlresolvers
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


class Industry(models.Model):
    name = models.CharField(default="", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "industries"


class Client(models.Model):
    name = models.CharField(default="", max_length=150)
    short_name = models.CharField(default="", max_length=50)
    slug = models.SlugField(default="", max_length=200)
    description = models.TextField(default="", blank=True, max_length=4000)
    date_description = models.CharField(default="", blank=True, max_length=100)
    display_on_frontend = models.BooleanField(default=False)
    enabled = models.BooleanField(default=True)
    address = models.ForeignKey('contact_info.Address',
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL,
                                related_name='address')
    contacts = models.ManyToManyField('contact_info.Person', blank=True)
    industries = models.ManyToManyField('Industry', blank=True)

    def link_to_address(self):
        """
        Returns link to edit the client's address record
        :param instance: current instance of this Client model
        :return: markup including anchor link to page to edit address record
        """
        if self.address:
            url = urlresolvers.reverse("admin:contact_info_address_change", args=[self.address.id])
            return u'<a href="%s">%s</a>' % (url, self.address)
        else:
            return 'n/a'
    link_to_address.allow_tags = True
    link_to_address.short_description = "Address"

    def link_to_frontend(self):
        if self.display_on_frontend:
            url = urlresolvers.reverse("client-details", args=[self.slug])
            return u'<a href="%s">%s</a>' % (url, self.slug)
        else:
            return 'n/a'
    link_to_frontend.allow_tags = True
    link_to_frontend.short_description = "Front-end page"

    def is_design_related(self):
        if 'DESIGN_INDUSTRY_TYPES' not in settings:
            raise ImproperlyConfigured('DESIGN_INDUSTRY_TYPES setting not found.')
        i = [item for item in self.industries.all() if item.name in settings.DESIGN_INDUSTRY_TYPES]
        return True if i else False

    def __str__(self):
        return self.name

    def get_industry_names(self):
        return [i.name for i in self.industries.all()]
