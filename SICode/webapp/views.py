from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.template.backends import django
from django.template.context_processors import csrf

from webapp.models import Employee, EmployeeForm
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

# def index(request):
#     return render(request, 'webapp/home.html')

def employees(request):
    return render_to_response('employees.html',
                              {'employees': Employee.objects.all()})

def employee(request, emp_id=1):
    return render_to_response('webapp/employee.html',
                              {'employee': Employee.objects.get(emp_id=emp_id)})


def create(request):
    if request.POST:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            csrf_token = django.middleware.csrf.get_token(request)
            form.save()

            return HttpResponseRedirect('.')
        else:
            form = EmployeeForm()

        # args = {}
        # args['form'] = form
        # args.update(csrf(request))
        # return render(request,'create_employee.html', args)
        return render_to_response('create_employee.html', {'form': form}, context_instance=RequestContext(request))