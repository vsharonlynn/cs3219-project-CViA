from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, list_route
from rest_framework.viewsets import ModelViewSet
from cvia.serializers import JobSerializer
from cvia.models import Job
from cvia.permissions import IsRecruiter


class JobViewSet(ModelViewSet):

    serializer_class = JobSerializer
    queryset = Job.objects.all()

    @permission_classes([IsAuthenticated, IsRecruiter])
    def create(self, request, *args, **kwargs):
        return ModelViewSet.create(self, request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
