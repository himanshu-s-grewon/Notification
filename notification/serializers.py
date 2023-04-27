from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


from notification.models import Notification




from user.choices import NotificationVerb





from user.models import Product

from user.serializers import ProductSerializer


class NotificationSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'verb', 'actor_type', 'target_id', 'title', 'description', 'user']

    def get_title(self, obj):
        if obj.verb == NotificationVerb.PRODUCT:
            return obj.target.name
        elif obj.verb == NotificationVerb.USER:
            return obj.actor.email
        elif obj.verb == NotificationVerb.ORDER:
            return obj.target.name
        else:
            return ' Select New Notification'

    def get_description(self, obj):
        if obj.verb == NotificationVerb.PRODUCT:
            return f'{obj.actor.username} added new Product'
        elif obj.verb == NotificationVerb.USER:
            return f'Welcome {obj.actor.email} Our App'
        elif obj.verb == NotificationVerb.ORDER:
            return f' {obj.actor.email} ordered your Product'
        else:
            return ' Select New Notification'

