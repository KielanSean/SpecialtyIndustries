from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group
from django.forms import ModelForm
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30, db_index=True)
    last_name = models.CharField(max_length=30, db_index=True)
    emp_id = models.CharField(max_length=9, primary_key=True, db_index=True)
    address = models.CharField(max_length=30, db_index=True)
    date_of_birth = models.DateField(blank=True, null=True, db_index=True)
    start_date = models.DateField(blank=True, null=True, db_index=True)
    active_status = models.BooleanField( db_index=True)
    phone_num = models.CharField(max_length=15, db_index=True)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.first_name + " " + self.last_name


class Standard(models.Model):
    standard_id = models.CharField(max_length=30, db_index=True)
    job_name = models.CharField(max_length=30,db_index=True)
    units_equal = models.IntegerField(db_index=True)
    num_steps = models.IntegerField(db_index=True)
    step_id = models.CharField(max_length=3, null=True, db_index=True)
    company_id = models.CharField(max_length=30, db_index=True, null=True)
    job_description = models.CharField(max_length=200, db_index=True, null=True)

    class Meta:
        db_table = "standard"

    def __str__(self):
        return self.standard_id + ": " + self.job_name


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'address', 'date_of_birth', 'start_date', 'phone_num']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }


class StandardForm(ModelForm):
    class Meta:
        model = Standard
        fields = ['standard_id', 'job_name', 'units_equal', 'num_steps']
        labels = {
            'standard_id': 'Standard Number',
            'job_name': 'Job',
        }


class Report(models.Model):
    step_id = models.CharField(max_length=3, db_index=True, null=True)
    standard_id = models.CharField(max_length=30, db_index=True)
    job_name = models.CharField(max_length=30, db_index=True)
    employee_name = models.CharField(max_length=40, db_index=True)
    piece_rate = models.IntegerField(db_index=True, null=True)
    hours = models.IntegerField(db_index=True, null=True)
    units_produced = models.IntegerField(db_index=True, null=True)
    absent = models.IntegerField(db_index=True)

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['step_id', 'piece_rate', 'standard_id', 'job_name', 'employee_name', 'hours', 'units_produced', 'absent']
        labels = {
            'step_id': 'Step Number',
            'piece_rate': 'Piece Rate',
            'standard_id': 'Standard Number',
            'job_name': 'Job',
            'employee_name': 'Employee Name',
            'hours': 'Hours',
            'units_produced': 'Units Produced',
            'absent': 'Absent',
        }




