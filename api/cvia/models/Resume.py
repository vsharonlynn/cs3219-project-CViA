from django.db.models import Model, AutoField, CharField, ForeignKey
from .user import User


class Resume(Model):
    id = AutoField(primary_key=True)
    author = ForeignKey(User, related_name='user')
    raw = CharField(max_length=1000, null=False)
