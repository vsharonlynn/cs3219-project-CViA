from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes as apply_permission_classes
from rest_framework.viewsets import ModelViewSet
from cvia.serializers import ResumeSerializer
from cvia.models import Resume
from cvia.permissions import IsEmployee


class ResumeViewSet(ModelViewSet):

    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Resume.objects.filter(author=self.request.user)

    @apply_permission_classes([IsAuthenticated, IsEmployee, ])
    def create(self, request, *args, **kwargs):
        return ModelViewSet.create(self, request, *args, **kwargs)

    @apply_permission_classes([IsAuthenticated, IsEmployee, ])
    def list(self, request, *args, **kwargs):
        return ModelViewSet.list(self, request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

