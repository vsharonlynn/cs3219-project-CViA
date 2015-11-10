from rest_framework.viewsets import ModelViewSet
from cvia.serializers import SubmissionSerializer
from cvia.models import Submission


class SubmissionViewSet(ModelViewSet):

    http_method_names = ['get', 'post', 'head']
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()