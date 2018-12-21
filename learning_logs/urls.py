"""Defines URL patterns for learning_logs."""
from django.conf.urls import url
from . import views

urlpatterns=[
    #Homepage
    url(r'^$', views.index, name='index'),

    # show all topics.
    url(r'^topics/$', views.topics, name='topics'),
]