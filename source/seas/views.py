from django.contrib.auth.models import User
from rest_framework import viewsets
from source.seas.models import ContentList
from source.seas.serializers import (
    ContentListSerializer,
    CurrentUserSerializer,
    UserProfileSerializer,
)
from source.seas.permissions import IsOwnerOrReadOnly
from rest_auth.views import LoginView


class CurrentUserView(LoginView):
    def get_response(self):
        original_response = super().get_response()
        current_user = User.objects.get(id=original_response.data["user"])
        current_user.api_token = original_response.data["key"]
        current_user_serializer = CurrentUserSerializer(current_user)
        original_response.data = current_user_serializer.data
        return original_response


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ContentListViewSet(viewsets.ModelViewSet):
    queryset = ContentList.objects.all()
    serializer_class = ContentListSerializer
    permission_classes = [IsOwnerOrReadOnly]
