from django.db.models import DateTimeField, ForeignKey, FileField, Model, AutoField
from .user import User


class FileUpload(Model):

    id = AutoField(primary_key=True)
    created = DateTimeField(auto_now_add=True)
    owner = ForeignKey(User, to_field='id')
    datafile = FileField()
