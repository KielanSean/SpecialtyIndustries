from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group
from django.db.models import Q
from django.forms import ModelForm
from django import forms
from django.urls import reverse
from django.utils import timezone
import datetime


# Create your models here.
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True, db_index=True)
    first_name = models.CharField(max_length=30, db_index=True)
    last_name = models.CharField(max_length=30, db_index=True)
    address = models.CharField(blank=True, max_length=30, db_index=True)
    date_of_birth = models.DateField(blank=True, null=True, db_index=True)
    start_date = models.DateField(blank=True, null=True, db_index=True)
    active_status = models.BooleanField( db_index=True, default=True)
    phone_num = models.CharField(blank=True, max_length=15, db_index=True)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.first_name + " " + self.last_name


class Standard(models.Model):
    standard_id = models.AutoField(primary_key=True, db_index=True)
    job_name = models.CharField(max_length=30,db_index=True)
    units_equal = models.IntegerField(db_index=True)
    num_steps = models.IntegerField(db_index=True)
    job_description = models.CharField(max_length=200, db_index=True, null=True)

    class Meta:
        db_table = "standard"

    def __str__(self):
        return self.job_name

class Step(models.Model):
    step_id = models.CharField(max_length=2, primary_key=True, db_index=True)
    standard_id = models.ForeignKey(Standard, db_index=True, on_delete=models.CASCADE)
    units_hr = models.IntegerField(db_index=True)
    time_each = models.DecimalField(decimal_places=2, max_digits=5, db_index=True)
    piece_rate = models.DecimalField(decimal_places=4, max_digits=5, db_index=True)

    class Meta:
        db_table = "step"

    def __str__(self):
        return self.step_id

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name','emp_id', 'address', 'date_of_birth', 'start_date', 'phone_num','active_status']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'emp_id': 'Employee ID',
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
    report_id = models.AutoField(primary_key=True, db_index=True)
    employee_name = models.ForeignKey(Employee, on_delete=models.CASCADE, limit_choices_to=Q(active_status=True))
    standard_id = models.ForeignKey(Standard, on_delete=models.CASCADE)
    step_id = models.ForeignKey(Step, on_delete=models.CASCADE)
    date_completed = models.DateField(db_index=True, default=datetime.date.today)
    job_name = models.CharField(max_length=30, db_index=True)
    piece_rate = models.DecimalField(decimal_places=4, max_digits=5, db_index=True)
    hours = models.IntegerField(db_index=True, null=True)
    units_produced = models.IntegerField(db_index=True, null=True)
    absent = models.IntegerField(db_index=True)

    def __str__(self):
        return self.date_completed.strftime('%m/%d/%Y') + " " + self.employee_name.last_name

    # def save(self):
    #     if not self.report_id:
    #         self.piece_rate = Step.piece_rate
    #         super(Report, self).save()

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['report_id', 'step_id', 'piece_rate', 'standard_id', 'job_name', 'employee_name', 'hours', 'units_produced', 'absent']
        labels = {
            'report_id': 'Report ID',
            'step_id': 'Step Number',
            'piece_rate': 'Piece Rate',
            'standard_id': 'Standard Number',
            'job_name': 'Job',
            'employee_name': 'Employee Name',
            'hours': 'Hours',
            'units_produced': 'Units Produced',
            'absent': 'Absent',
        }




