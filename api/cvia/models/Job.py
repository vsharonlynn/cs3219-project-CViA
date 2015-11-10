from django.db.models import Model, AutoField, CharField, ForeignKey, FileField, DateTimeField
from .user import User


class Job(Model):

    id = AutoField(primary_key=True)
    author = ForeignKey(User, related_name='author', to_field='id')
    title = CharField(max_length=255, null=False)
    description = CharField(max_length=1000, null=False)
    raw = FileField()
    createdAt = DateTimeField(auto_now_add=True)
