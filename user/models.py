import datetime
import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from user.choices import Usertype
from user.managers import UserManager


class User(AbstractUser):
    email = models.EmailField('Email Address', unique=True)
    username = models.CharField('Username', blank=True, max_length=40)
    first_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)
    user_type = models.CharField(max_length=100, choices=Usertype.choices)
    notifications = GenericRelation("notification.Notification", content_type_field='actor_type_id',
                                    object_id_field='actor_id')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.pk}'


class Product(models.Model):
    from notification.models import Notification

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_product')
    name = models.CharField(max_length=100, help_text='Product Name')
    product_id = models.IntegerField()
    price = models.IntegerField()
    notifications = GenericRelation(Notification, content_type_field='target_type_id',
                                    object_id_field='target_id', )

    def __str__(self):
        return f'{self.id}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_order')
    date = models.DateTimeField(auto_now_add=True)
    order_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    confirmed = models.BooleanField(default=False)
    notifications = GenericRelation("notification.Notification", content_type_field='action_object_type_id',
                                    object_id_field='action_object_id', )


    def __str__(self):
        return self.product.name
