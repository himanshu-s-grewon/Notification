from celery import shared_task
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

from notification.models import Notification
from user.choices import NotificationVerb, Usertype
from user.models import User, Product, Order


# SEnd only which one Created
@shared_task
def send_user_notification(user_id):
    try:
        user = User.objects.get(id=user_id)
        Notification.objects.create(verb=NotificationVerb.USER,
                                    actor_id=user_id,
                                    actor_type=ContentType.objects.get_for_model(User),
                                    user=user)
        return "Working"
    except Exception as e:
        print(e)


# #For Send notification all User exclude Which one created
# @shared_task
# def send_notification(user_id):
#     try:
#         for user in User.objects.exclude(id=user_id):
#             Notification.objects.create(verb=NotificationVerb.USER, actor_id=user_id,
#                                         actor_type=ContentType.objects.get_for_model(User),
#                                         user=user)
#         return "Working"
#     except Exception as e:
#         print(e)


@shared_task
def send_product_notification(pro_id):
    product = Product.objects.get(pk=pro_id)
    try:
        for user in User.objects.exclude(Q(id=product.user_id) | Q(user_type=Usertype.SUPPLIER)):
            Notification.objects.create(verb=NotificationVerb.PRODUCT, actor_id=product.user_id,
                                        actor_type=ContentType.objects.get_for_model(User),
                                        target_id=product.id,
                                        target_type=ContentType.objects.get_for_model(Product),
                                        user=user)
        return "Working"
    except Exception as e:
        print(e)


@shared_task
def send_order_notification(ord_id):
    order = Order.objects.get(pk=ord_id)
    try:
        Notification.objects.create(verb=NotificationVerb.ORDER,
                                    actor_type=ContentType.objects.get_for_model(User),
                                    actor_id=order.user_id,
                                    target_type=ContentType.objects.get_for_model(Product),
                                    target_id=order.product_id,
                                    action_object_type=ContentType.objects.get_for_model(Order),
                                    action_object_id=order.id,
                                    user=order.product.user)
        print('Created')
        return "Working"
    except Exception as e:
        print(e,'>>>>>>>>>>>>>>>')
