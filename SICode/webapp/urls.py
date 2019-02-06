from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^forgot$', views.forgot, name='forgot'),
    url(r'^signup$', views.signup, name='signup'),
]