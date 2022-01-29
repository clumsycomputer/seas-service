from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from source.seas.models import ContentList
from source.seas.serializers import ContentListSerializer, UserSerializer
from source.seas.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContentListViewSet(viewsets.ModelViewSet):
    queryset = ContentList.objects.all()
    serializer_class = ContentListSerializer
    permission_classes = [IsOwnerOrReadOnly]
