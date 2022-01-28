from email.policy import default
from django.contrib.auth.models import User
from django.db import models


class ContentList(models.Model):
    contentListAuthor = models.ForeignKey(
        User,
        default=1,
        on_delete=models.CASCADE,
        related_name='contentLists')
    contentListTitle = models.CharField(max_length=50)
    contentListRating = models.CharField(
        choices=(
            ('SUITABLE_FOR_WORK', 'suitableForWork'),
            ('NOT_SUITABLE_FOR_WORK', 'notSuitableForWork')),
        default='SUITABLE_FOR_WORK',
        max_length=50)


class ContentItem(models.Model):
    contentList = models.ForeignKey(
        ContentList,
        default=1,
        on_delete=models.CASCADE,
        related_name='contentListItems')
    contentItemTitle = models.CharField(max_length=50)
    contentItemAuthor = models.CharField(max_length=50)


class ContentLink(models.Model):
    contentItem = models.ForeignKey(
        ContentItem,
        default=1,
        on_delete=models.CASCADE,
        related_name='contentItemLinks')
    contentLinkHostName = models.CharField(max_length=50, default="todo")
    contentLinkUrl = models.URLField(max_length=200, default="todo")
