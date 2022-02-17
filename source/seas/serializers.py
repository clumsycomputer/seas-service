from email.policy import default
from django.contrib.auth.models import User
from rest_framework import serializers
from source.seas.models import ContentList, ContentItem, ContentLink
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_auth.serializers import TokenSerializer
from rest_auth.models import TokenModel
from django.forms import ValidationError


class UserProfileContentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentList
        fields = ["content_list_title", "content_list_rating"]


class UserProfileSerializer(serializers.ModelSerializer):
    content_lists = UserProfileContentListSerializer(
        many=True, read_only=True, default=[]
    )

    class Meta:
        model = User
        fields = ["username", "content_lists"]


class CurrentUserTokenSerializer(TokenSerializer):
    class Meta:
        model = TokenModel
        fields = ["key", "user"]


class CurrentUserSerializer(serializers.ModelSerializer):
    api_token = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ["username", "email", "api_token"]


class ContentListAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


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
            "content_list_author",
            "content_list_title",
            "content_list_rating",
            "content_list_items",
        ]

    def validate_content_list_title(self, value):
        content_list_title_exist = (
            ContentList.objects.all()
            .filter(
                content_list_author=self.context["request"].user,
                content_list_title=value,
            )
            .exists()
        )
        if content_list_title_exist:
            raise ValidationError("title already exists")
        return value
