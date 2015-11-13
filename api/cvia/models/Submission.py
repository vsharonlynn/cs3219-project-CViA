from django.db.models import Model, AutoField, ForeignKey, DateTimeField, FloatField
from .resume import Resume
from .job import Job


class Submission(Model):

    id = AutoField(primary_key=True)
    resume = ForeignKey(Resume, related_name='resume')
    job = ForeignKey(Job, related_name='job')
    created_at = DateTimeField(auto_now_add=True)
    score_1 = FloatField(null=True, default=0)
    score_2 = FloatField(null=True, default=0)
    score_3 = FloatField(null=True, default=0)
    score_4 = FloatField(null=True, default=0)
    max_score = FloatField(null=True, default=0)
