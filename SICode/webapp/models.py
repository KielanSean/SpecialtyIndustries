from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group
from django.forms import ModelForm
from django.urls import reverse
from django.utils import timezone




# Create your models here.

class Employee(models.Model):
    f_name = models.CharField(max_length=30, db_index=True)
    l_name = models.CharField(max_length=30, db_index=True)
    emp_id = models.CharField(max_length=9, primary_key=True, db_index=True)
    address = models.CharField(max_length=30, db_index=True)
    date_of_birth = models.DateField(blank=True, null=True, db_index=True)
    start_date = models.DateField(blank=True, null=True, db_index=True)
    active_status = models.BooleanField( db_index=True)
    phone_num = models.CharField(max_length=15, db_index=True)


    def __str__(self):
        return self.f_name + self.l_name

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['f_name', 'l_name', 'address','date_of_birth','start_date','phone_num']
        labels = {
            'f_name': ('First Name'),
            'l_name': ('Last Name'),
        }