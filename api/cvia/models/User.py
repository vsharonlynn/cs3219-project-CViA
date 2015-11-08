from django.db.models import AutoField, CharField
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(PermissionsMixin, AbstractBaseUser):
    id = AutoField(primary_key=True)
    username = CharField(max_length=255, unique=True, null=True,
                         db_index=True)
    first_name = CharField(max_length=255, default="Anonymous")
    last_name = CharField(max_length=255, default="Person")
    email = CharField(max_length=255)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()
