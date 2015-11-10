from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField
from cvia.models import Job


class JobSerializer(HyperlinkedModelSerializer):

    author = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Job
        fields = ('id', 'author', 'title', 'description', 'raw', 'createdAt')
