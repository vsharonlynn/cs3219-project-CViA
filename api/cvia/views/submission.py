from rest_framework.viewsets import ModelViewSet
from cvia.serializers import SubmissionSerializer
from cvia.models import Submission


class SubmissionViewSet(ModelViewSet):
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()