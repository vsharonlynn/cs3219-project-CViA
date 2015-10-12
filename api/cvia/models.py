from django.db import models

class JobDescription(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)

class Cv(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='cvs')
    job_description = models.ForeignKey(JobDescription, related_name='cvs')
    raw = models.FileField(upload_to='raw/')
