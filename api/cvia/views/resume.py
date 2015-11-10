from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes as apply_permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FormParser, MultiPartParser
from cvia.serializers import ResumeSerializer
from cvia.models import Resume
from cvia.permissions import IsEmployee


class ResumeViewSet(ModelViewSet):

    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )

    @apply_permission_classes([IsAuthenticated, IsEmployee, ])
    def create(self, request, *args, **kwargs):
        return ModelViewSet.create(self, request, *args, **kwargs)

    @apply_permission_classes([IsAuthenticated, IsEmployee, ])
    def list(self, request, *args, **kwargs):
        queryset = Resume.objects.filter(author=request.user)
        return ModelViewSet.list(self, request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        title=self.request.data.get('title'),
                        raw=self.request.data.get('raw'))
