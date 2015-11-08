from rest_framework.serializers import ModelSerializer
from cvia.models import Resume
from .user import UserSerializer


class ResumeSerializer(ModelSerializer):
    author = UserSerializer

    class Meta:
        model = Resume
        fields = ('id', 'author', 'raw')