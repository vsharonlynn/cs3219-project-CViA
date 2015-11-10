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
    createdAt = DateTimeField(auto_now_add=True)
