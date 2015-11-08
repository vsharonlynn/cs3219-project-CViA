from django.db.models import Model, AutoField, ForeignKey
from .resume import Resume
from .job import Job
from .user import User


class Submission(Model):
    id = AutoField(primary_key=True)
    resume = ForeignKey(Resume, related_name='resume')
    job = ForeignKey(Job, related_name='job')