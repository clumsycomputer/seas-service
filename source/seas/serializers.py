from email.policy import default
from django.contrib.auth.models import User
from rest_framework import serializers
from source.seas.models import ContentList, ContentItem, ContentLink
from drf_writable_nested.serializers import WritableNestedModelSerializer


class UserContentListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentList
        fields = ['id', 'contentListTitle', 'contentListRating']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    contentLists = UserContentListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'contentLists']


class ContentListAuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ContentLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentLink
        fields = ['contentLinkHostName', 'contentLinkUrl']


class ContentItemsSerializer(WritableNestedModelSerializer):
    contentItemLinks = ContentLinkSerializer(many=True, default=[])

    class Meta:
        model = ContentItem
        fields = ['contentItemTitle', 'contentItemAuthor', 'contentItemLinks']


class ContentListSerializer(WritableNestedModelSerializer):
    contentListAuthor = ContentListAuthorSerializer(read_only=True)
    contentListItems = ContentItemsSerializer(many=True, default=[])

    class Meta:
        model = ContentList
        fields = ['id', 'contentListAuthor', 'contentListTitle',
                  'contentListRating', 'contentListItems']
