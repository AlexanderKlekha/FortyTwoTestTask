from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()

    # Contacts
    email = models.CharField(max_length=30)
    jabber = models.CharField(max_length=30)
    skype = models.CharField(max_length=20)
    other_contact = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s %s" % (self.last_name, self.first_name)
