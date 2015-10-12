from rest_framework import serializers
from .models import JobDescription, User, Cv

class CvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cv
        fields = ('id', 'job_description', 'user')

class JobDescriptionSerializer(serializers.ModelSerializer):
    cvs = CvSerializer

    class Meta:
        model = JobDescription
        fields = ('id', 'title', 'cvs')

class UserSerializer(serializers.ModelSerializer):
    cvs = CvSerializer

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'cvs')
