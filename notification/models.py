from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from user.choices import NotificationVerb
from user.models import User


# Create your models here.


class Notification(models.Model):
    verb = models.CharField(max_length=100, choices=NotificationVerb.choices)
    actor_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='actor_type_activities')
    actor_id = models.PositiveIntegerField(null=True, blank=True)
    actor = GenericForeignKey('actor_type', 'actor_id')
    target_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='target_type_activities',
                                    null=True, blank=True)
    target_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_type', 'target_id')
    action_object_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                           related_name='action_object_type_activities', null=True, blank=True)
    action_object_id = models.PositiveIntegerField(null=True, blank=True)
    action_object = GenericForeignKey('action_object_type', 'action_object_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.verb}'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
