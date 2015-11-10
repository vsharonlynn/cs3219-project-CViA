from django.db.models import Model, AutoField, ForeignKey, DateTimeField, FloatField
from .resume import Resume
from .job import Job


class Submission(Model):

    id = AutoField(primary_key=True)
    resume = ForeignKey(Resume, related_name='resume')
    job = ForeignKey(Job, related_name='job')
    createdAt = DateTimeField(auto_now_add=True)
    score = FloatField(null=True, default=0)
    max_score = FloatField(null=True, default=0)
