from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from cvia.models import Resume


class ResumeSerializer(ModelSerializer):

    author = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Resume
        fields = ('id', 'title', 'raw', 'author', 'created_at')
