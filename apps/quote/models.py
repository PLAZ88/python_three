from __future__ import unicode_literals

from django.db import models
from ..log_reg.models import User


class Quote(models.Model):
    quote = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, related_name = "quotes", blank=True, null=True)
    # objects = QuoteManager()


class Favorite(models.Model):

    quote = models.ForeignKey(Quote, related_name="quote_favorite", blank=True, null=True)
    users = models.ForeignKey(User, related_name="user_favorites", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
