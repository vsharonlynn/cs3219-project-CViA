from rest_framework.viewsets import ModelViewSet
from cvia.serializers import UserSerializer
from cvia.models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()