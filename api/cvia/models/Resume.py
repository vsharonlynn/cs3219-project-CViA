from django.db.models import Model, AutoField, CharField, ForeignKey, DateTimeField
from .user import User
from .file_upload import FileUpload


class Resume(Model):

    id = AutoField(primary_key=True)
    title = CharField(max_length=255, null=False)
    author = ForeignKey(User, related_name='user')
    raw = ForeignKey(FileUpload, null=False)
    created_at = DateTimeField(auto_now_add=True)
