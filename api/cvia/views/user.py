from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes, list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from cvia.permissions import IsSelf
from cvia.serializers import UserSerializer
from cvia.models import User


class UserViewSet(ModelViewSet):

    http_method_names = ['head', 'get', 'put', 'options']
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @permission_classes([IsSelf])
    def update(self, request, *args, **kwargs):
        return ModelViewSet.update(self, request, *args, **kwargs)

    @list_route(methods=['get'])
    @permission_classes([IsAuthenticated])
    def current(self, request, *args, **kwargs):
        serialized = UserSerializer(request.user)
        return Response(serialized.data)
