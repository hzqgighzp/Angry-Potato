#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '1.0.0.0'


import re
from django import forms
from django.core.exceptions import ValidationError




class RegisterForm(forms.Form):
    uname = forms.CharField(required=True, error_messages={"invalid": u"Username format is wrong!", "required": "Username cannot be empty!"})
    email = forms.EmailField(required=True, error_messages={"invalid": u"E-mail format is wrong!", "required": "E-mail cannot be empty!"})
    pwd = forms.CharField(required=True, min_length=5, error_messages={"invalid": u"The password is invalid and must be more than 5 characters",
                                                                       "required": "The password cannot be empty!"})


class LoginForm(forms.Form):
    uname = forms.CharField(required=True)
    pwd = forms.CharField(required=True, min_length=5)

