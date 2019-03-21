from django.test import TestCase
from myapp.models import ClassifyModel
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from custom_user.forms import RegisterForm, LoginForm
from custom_user.models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.test import Client
User = get_user_model()
# Create your tests here.

class ClassifyMethodTests(TestCase):
    def test_ensure_classify_are_not_empty(self):
        cat = ClassifyModel(name='')
        cat.save()
        self.assertEqual((cat.name != ''), True)

class IndexViewTests(TestCase):
    def test_index_view_when_not_login(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign in")
        self.assertContains(response, "Sign up")

class LoginTests(TestCase):
    def test_user_log_in(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c = Client()
        login = c.login(username='testuser', password='12345')
        self.assertTrue(login)

            