from rest_framework.viewsets import ModelViewSet
from cvia.serializers import JobSerializer
from cvia.models import Job


class JobViewSet(ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
