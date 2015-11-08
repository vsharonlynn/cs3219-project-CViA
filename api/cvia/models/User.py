from django.db.models import Model, AutoField, CharField


class User(Model):
    id = AutoField(primary_key=True)
    email = CharField(max_length=255, null=False)
    password = CharField(max_length=255, null=False)