from rest_framework.serializers import ModelSerializer
from cvia.models import Submission
from .job import JobSerializer
from .resume import ResumeSerializer


class SubmissionSerializer(ModelSerializer):
    resume = ResumeSerializer
    job = JobSerializer

    class Meta:
        model = Submission
        fields = ('id', 'resume', 'job')
