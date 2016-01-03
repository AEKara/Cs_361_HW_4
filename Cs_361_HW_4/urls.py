"""Cs_361_HW_4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls import url
from Design_Page import views

urlpatterns = [


    url(r'^add_teacher/$', views.add_teacher),
    url(r'^add_student/$', views.add_student),
    url(r'^add_course/$', views.add_course),

    url(r'^all_teachers/', views.all_teachers),
    url(r'^all_students/', views.all_students),
    url(r'^all_courses/', views.all_courses),
    url(r'^enroll/', views.enroll),

]