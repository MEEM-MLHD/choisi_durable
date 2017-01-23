# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin

from projects.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
]

admin.site.site_header = "Habitat choisi et durable"