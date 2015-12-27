from django.contrib import admin

# Register your models here.

from models import *


class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Person',
         {'fields':  ['first_name', 'last_name', 'date_of_birth']}),
        ('Contact Info',
         {'fields':  ['email', 'jabber', 'skype', 'other_contact']}),
    ]
    list_display = ('last_name', 'first_name', 'date_of_birth')

    search_fields = ('last_name', 'first_name', 'date_of_birth')
    list_filter = ['last_name']

admin.site.register(Person, PersonAdmin)