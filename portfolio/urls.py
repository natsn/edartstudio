from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view()),
    url(r'^portfolios', Portfolios.as_view()),
)
