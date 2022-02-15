from email.policy import default
from django.contrib.auth.models import User
from django.db import models


class ContentList(models.Model):
    content_list_author = models.ForeignKey(
        User, default=1, on_delete=models.CASCADE, related_name="content_lists"
    )
    content_list_title = models.CharField(max_length=50)
    content_list_rating = models.CharField(
        choices=(
            ("SAFE_FOR_WORK", "safeForWork"),
            ("NOT_SAFE_FOR_WORK", "notSafeForWork"),
        ),
        default="SAFE_FOR_WORK",
        max_length=50,
    )


class ContentItem(models.Model):
    content_list = models.ForeignKey(
        ContentList,
        default=1,
        on_delete=models.CASCADE,
        related_name="content_list_items",
    )
    content_item_title = models.CharField(max_length=50)
    content_item_author = models.CharField(max_length=50)


class ContentLink(models.Model):
    content_item = models.ForeignKey(
        ContentItem,
        default=1,
        on_delete=models.CASCADE,
        related_name="content_item_links",
    )
    content_link_host_name = models.CharField(max_length=50)
    content_link_url = models.URLField(max_length=200)
