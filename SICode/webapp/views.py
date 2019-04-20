from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.template.backends import django
from django.contrib.auth import logout
from django.views.generic import TemplateView, UpdateView
from SICode.webapp.models import Employee
# from .forms import EmployeeForm

from django.template.context_processors import csrf


from .models import Employee, EmployeeForm, Standard, StandardForm
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

# def index(request):
#     return render(request, 'webapp/home.html')

# def employees(request):
#     return render_to_response('employees.html',
#                               {'employees': Employee.objects.all()})



# def standards(requesr):
#     return render_to_response('standards': Standard.objects.all())


# def employee(request, emp_id=1):
#     return render_to_response('webapp/employee.html',
#                               {'employee': Employee.objects.get(emp_id=emp_id)})


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


def forgot(request):
    return render(request, 'webapp/page-forget.html')


def signup(request):
    return render(request, 'webapp/page-register.html')


def index(request):
    return render(request, 'webapp/index.html')


def adminindex(request):
    return render(request, 'webapp/index2.html')


def biweekly(request):
    return render(request, 'webapp/biweeklyforms.html')


def admin_biweekly(request):
    return render(request, 'webapp/biweeklyformsadmin.html')


def production(request):
    return render(request, 'webapp/productionforms.html')


def admin_production(request):
    return render(request, 'webapp/productionformsadmin.html')


def logout_view(request):
    logout(request)


def report_view(request):
    return render(request, 'webapp/reportshome.html')


def employee_view(request):
    return render(request, 'webapp/employeehome.html')


def standard_view(request):
    return render(request, 'webapp/standardshome.html')


def create_standard(request):
    if request.method == "POST":
        form = StandardForm(request.POST)
        if form.is_valid():
            form.save()

    form = StandardForm
    return render(request, 'webapp/createstandard.html', {'form':form})


def view_standards(request):
    stands = Standard.objects.all()
    args = {'stands': stands}
    return render(request, 'webapp/viewstandard.html', args)


def testemp(request):

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            print("VALID")

            form.save()

    form = EmployeeForm
    return render(request, 'webapp/testemp.html', {'form': form})


def testempview(request):
    emps = Employee.objects.all()
    args = {'emps': emps}
    return render(request, 'webapp/testempview.html',args)


def EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['first_name']









