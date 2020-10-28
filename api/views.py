from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, GroupSerializer
# Create your views here.

# all methods will be there
class UserAPIView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

# if you set generics view then you have to define view in url according
# only for get and post
class GroupAPIView(ListCreateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

# only for retrive,delete,put
class GroupDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
