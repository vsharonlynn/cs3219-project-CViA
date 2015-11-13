from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField
from cvia.models import FileUpload


class FileUploadSerializer(HyperlinkedModelSerializer):
    owner = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = FileUpload
        fields = ('id', 'created', 'datafile', 'owner')
        read_only_fields = ('created', 'datafile', 'owner')
