from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django import forms
# Create your models here.


class SynergyUser(User):
    STATUSES = ((0, 'Inactive'),
                (1, 'Active'))

    phone = models.CharField(max_length=40)
    mobile = models.CharField(max_length=40)
    status = models.IntegerField(choices=STATUSES)


class SynergyUserForm(forms.ModelForm):

    class Meta:
        model = SynergyUser
        fields = ['username', 'email', 'phone', 'mobile', 'status']


class SynergyCourse(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=20)
    users = models.ManyToManyField(SynergyUser, blank=True)


admin.site.register(SynergyUser)
admin.site.register(SynergyCourse)
