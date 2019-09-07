
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from walls.models import Route, Sector, Area


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    sector_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='sector-detail'
    )

    class Meta:
        model = Area
        fields = ['url', 'name', 'sector_set', ]


class SectorSerializer(serializers.HyperlinkedModelSerializer):
    route_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='route-detail'
    )

    class Meta:
        model = Sector
        fields = ['url', 'name', 'area', 'route_set']
        depth = 1


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.CharField(source='get_type_display')
    degree = serializers.StringRelatedField()

    class Meta:
        model = Route
        fields = ['url', 'uuid', 'name', 'sector', 'sectors_by', 'degree', 'type']
