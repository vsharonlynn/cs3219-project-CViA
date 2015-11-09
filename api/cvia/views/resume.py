from rest_framework.viewsets import ModelViewSet
from cvia.serializers import ResumeSerializer
from cvia.models import Resume


class ResumeViewSet(ModelViewSet):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()