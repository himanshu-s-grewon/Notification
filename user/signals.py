from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_delete
from django.dispatch import receiver

from notification.models import Notification
from user.models import Product

#
# @receiver(post_delete, sender=Product)
# def product_delete_notification(sender, instance,*args, **kwargs):
#     c_type = ContentType.objects.get_for_model(sender)
#     obj = Notification.objects.filter(target_type=c_type,target_id=instance.id)
#     print(obj)
#     obj.delete()
#     print("done")