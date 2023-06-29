from rest_framework import viewsets

from core.models import User

from .serializers import ListUserSerializer


class UsersViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ListUserSerializer()
