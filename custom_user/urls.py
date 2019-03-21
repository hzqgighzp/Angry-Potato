#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '1.0.0.0'

"""
@brief 简介 
@details 详细信息
@author  niuniuc
@data    2019-02-02 
"""
from django.conf.urls import url
from . import views
from .views import RegisterView, LoginView, LogoutView,DetailView

urlpatterns = [
    url('register/', RegisterView.as_view(), name="register"),
    url('login/', LoginView.as_view(), name="login"),
    url('logout/', LogoutView.as_view(), name="logout"),
    url('detail/', DetailView.as_view(), name="detail"),
    url('facebook/', views.facebook, name='facebook'),

]