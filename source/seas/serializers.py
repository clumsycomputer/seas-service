from django.contrib.auth.models import User
from rest_framework import serializers
from source.seas.models import ContentList, ContentItem, ContentLink
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_auth.serializers import TokenSerializer
from rest_auth.models import TokenModel


class UserProfileContentListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentList
        fields = ["id", "contentListTitle", "contentListRating"]


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    contentLists = UserProfileContentListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "contentLists"]


class CurrentUserTokenSerializer(TokenSerializer):
    class Meta:
        model = TokenModel
        fields = ["key", "user"]


class CurrentUserSerializer(serializers.ModelSerializer):
    authToken = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "authToken"]


class ContentListAuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class ContentLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentLink
        fields = ["contentLinkHostName", "contentLinkUrl"]


class ContentItemsSerializer(WritableNestedModelSerializer):
    contentItemLinks = ContentLinkSerializer(many=True, default=[])

    class Meta:
        model = ContentItem
        fields = ["contentItemTitle", "contentItemAuthor", "contentItemLinks"]


class ContentListSerializer(WritableNestedModelSerializer):
    contentListAuthor = ContentListAuthorSerializer(read_only=True)
    contentListItems = ContentItemsSerializer(many=True, default=[])

    class Meta:
        model = ContentList
        fields = [
            "id",
            "contentListAuthor",
            "contentListTitle",
            "contentListRating",
            "contentListItems",
        ]
