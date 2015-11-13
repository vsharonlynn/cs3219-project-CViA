from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from cvia.models import Job


class JobSerializer(ModelSerializer):

    author = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Job
        fields = ('id', 'author', 'title', 'description', 'raw', 'created_at')

