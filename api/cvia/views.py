from rest_framework import viewsets
from .models import JobDescription, User, Cv
from .serializers import JobDescriptionSerializer, \
                         UserSerializer, \
                         CvSerializer

class JobDescriptionViewSet(viewsets.ModelViewSet):
    serializer_class = JobDescriptionSerializer
    queryset = JobDescription.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class CvViewSet(viewsets.ModelViewSet):
    serializer_class = CvSerializer
    queryset = Cv.objects.all()
