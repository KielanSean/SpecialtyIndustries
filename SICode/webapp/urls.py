from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    url(r'^login/$', auth_views.auth_login, {'template_name': 'page-login.html'}, name='login'),
    url(r'^logout/$', LogoutView.as_view(), {'next_page': 'base.html'}, name='logout'),
    url(r'^forgot/$', views.forgot, name='forgot'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^index/$', views.index, name='index'),
    url(r'^adminindex/$', views.adminindex, name='adminindex'),
    url(r'^biweekly/$', views.biweekly, name='biweekly'),
    url(r'^production/$', views.production, name='production'),
    url(r'^admin_biweekly/$', views.admin_biweekly, name='admin_biweekly'),
    url(r'^admin_production/$', views.admin_production, name='admin_production'),
    url(r'^standard_view/$', views.standard_view, name='standard_view'),
    url(r'^employees/$', views.employee_view, name='employee_view'),
    url(r'^report_view/$', views.report_view, name='report_view'),
    url(r'^testemp/$', views.testemp, name='testemp'),
    url(r'^testempview/$',views.testempview, name='testempview'),
    url(r'^createstandard/$',views.create_standard,name='createstandard'),
    url(r'^viewstandard/$',views.view_standards,name='viewstandard'),







]