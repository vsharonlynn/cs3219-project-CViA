from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from cvia.models import Submission


class SubmissionSerializer(ModelSerializer):

    resume = PrimaryKeyRelatedField(read_only=True)
    job = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Submission
        fields = ('id', 'resume', 'job', 'created_at')
