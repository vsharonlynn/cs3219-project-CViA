from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.viewsets import ModelViewSet
from cvia.serializers import JobSerializer
from cvia.models import Job
from cvia.permissions import IsRecruiter


class MyJobViewSet(ModelViewSet):

    serializer_class = JobSerializer
    queryset = Job.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, IsRecruiter)

    def get_queryset(self):
        return Job.objects.filter(author=self.request.user)
