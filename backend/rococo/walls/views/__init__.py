from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from walls.serializers import UserSerializer, GroupSerializer, RouteSerializer, AreaSerializer, SectorSerializer
from walls.models import Route, Sector, Area


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class SectorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer


class RouteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
