from django.db.models import Model, AutoField, CharField, ForeignKey, DateTimeField, FileField
from .user import User


class Resume(Model):

    id = AutoField(primary_key=True)
    title = CharField(max_length=255, null=False)
    author = ForeignKey(User, related_name='user')
    raw = FileField()
    createdAt = DateTimeField(auto_now_add=True)
