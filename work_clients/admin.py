from django.core import urlresolvers
from django.contrib import admin
from work_clients.models import Client, Industry


class ContactInline(admin.TabularInline):
    model = Client.contacts.through


class IndustryInline(admin.TabularInline):
    model = Client.industries.through
    extra = 1


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'date_description', 'link_to_address', 'link_to_frontend', 'enabled', ]
    prepopulated_fields = {'slug': ('name',)}
    inline_type = 'stacked'

    inlines = [ContactInline, IndustryInline, ]
    exclude = ['contacts', 'industries', ]


admin.site.register(Client, ClientAdmin)

admin.site.register(Industry)
