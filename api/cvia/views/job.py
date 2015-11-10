from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FormParser, MultiPartParser
from cvia.serializers import JobSerializer
from cvia.models import Job, User
from cvia.permissions import IsRecruiter


class JobViewSet(ModelViewSet):

    serializer_class = JobSerializer
    queryset = Job.objects.all()
    parser_classes = (MultiPartParser, FormParser)

    @permission_classes([IsAuthenticated, IsRecruiter])
    def create(self, request, *args, **kwargs):
        return ModelViewSet.create(self, request, *args, **kwargs)

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(author=user,
                        title=self.request.data.get('title'),
                        description=self.request.data.get('description'),
                        raw=self.request.data.get('raw'))
