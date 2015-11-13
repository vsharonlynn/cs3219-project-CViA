from django import forms
from django.db.models import AutoField, CharField, EmailField, DateTimeField
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(PermissionsMixin, AbstractBaseUser):

    id = AutoField(primary_key=True)
    username = CharField(max_length=255, blank=True)
    first_name = CharField(max_length=255, default="Anonymous")
    last_name = CharField(max_length=255, default="Person")
    email = EmailField(max_length=255, unique=True)
    role = CharField(max_length=20, default='Employee', choices=(
        ('Employee', 'Employee'),
        ('Recruiter', 'Recruiter')))
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']
    objects = UserManager()
    created_at = DateTimeField(auto_now_add=True)


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    role = forms.CharField(max_length=20)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.role = self.cleaned_data['role']
        user.save()
