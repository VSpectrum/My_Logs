from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<filter_word>([A-Za-z0-9_\.-]+))/$$', views.filter, name='filter'),
]