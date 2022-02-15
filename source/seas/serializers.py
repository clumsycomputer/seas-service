from django.contrib.auth.models import User
from rest_framework import serializers
from source.seas.models import ContentList, ContentItem, ContentLink
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_auth.serializers import TokenSerializer
from rest_auth.models import TokenModel


class UserProfileContentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentList
        fields = ["id", "content_list_title", "content_list_rating"]


class UserProfileSerializer(serializers.ModelSerializer):
    content_lists = UserProfileContentListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "content_lists"]


class CurrentUserTokenSerializer(TokenSerializer):
    class Meta:
        model = TokenModel
        fields = ["key", "user"]


class CurrentUserSerializer(serializers.ModelSerializer):
    api_token = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "api_token"]


class ContentListAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class ContentLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentLink
        fields = ["content_link_host_name", "content_link_url"]


class ContentItemsSerializer(WritableNestedModelSerializer):
    content_item_links = ContentLinkSerializer(many=True, default=[])

    class Meta:
        model = ContentItem
        fields = ["content_item_title", "content_item_author", "content_item_links"]


class ContentListSerializer(WritableNestedModelSerializer):
    content_list_author = ContentListAuthorSerializer(read_only=True)
    content_list_items = ContentItemsSerializer(many=True, default=[])

    class Meta:
        model = ContentList
        fields = [
            "id",
            "content_list_author",
            "content_list_title",
            "content_list_rating",
            "content_list_items",
        ]
