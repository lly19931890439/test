from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index' ),
    url(r'^calzeta$', views.calzeta, name='calzeta'),
    url(r'^calages$', views.calages, name='calages'),
    url(r'^image$', views.image, name='image')
]
