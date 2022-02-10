from background.models import ListThings,User
from rest_framework import  serializers, viewsets
# Create your views here.

# Serializers define the API representation.
class ThingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ListThings
        fields = ['things_id', 'userid', 'date', 'process', 'emotion', 'energy', 'key']

# ViewSets define the view behavior.
class ThingsViewSet(viewsets.ModelViewSet):
    queryset = ListThings.objects.all()
    serializer_class = ThingsSerializer

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'user_name', 'user_passwd']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
