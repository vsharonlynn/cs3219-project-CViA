from rest_framework.serializers import ModelSerializer
from cvia.models import Job
from .user import UserSerializer


class JobSerializer(ModelSerializer):
    author = UserSerializer

    class Meta:
        model = Job
        fields = ('id', 'author', 'title', 'description', 'raw')