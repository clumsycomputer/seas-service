from django.contrib.auth.models import User
from drf_writable_nested import serializers
from rest_framework import viewsets, views
from rest_framework.response import Response
from source.seas.models import ContentList
from source.seas.serializers import ContentListSerializer, CurrentUserSerializer, UserProfileSerializer
from source.seas.permissions import IsOwnerOrReadOnly


class CurrentUserView(views.APIView):
    def get(self, request):
        serializer = CurrentUserSerializer(request.user)
        return Response(serializer.data)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ContentListViewSet(viewsets.ModelViewSet):
    queryset = ContentList.objects.all()
    serializer_class = ContentListSerializer
    permission_classes = [IsOwnerOrReadOnly]
