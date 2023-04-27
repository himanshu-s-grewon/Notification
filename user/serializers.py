from rest_framework import serializers
from user.models import User, Product, Order
from user.tasks import send_user_notification, send_product_notification, send_order_notification


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username', 'is_active', 'user_type']
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            is_active=validated_data['is_active'],
            user_type=validated_data['user_type'],
        )
        user.set_password(validated_data['password'])
        user.save()
        send_user_notification(user.id)
        return user
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'product_id', 'price', 'user']

    def create(self, validated_data):
        product = Product.objects.create(
            name=validated_data['name'],
            product_id=validated_data['product_id'],
            price=validated_data['price'],
            user=validated_data['user'],
        )
        product.save()
        send_product_notification(product.id)
        return product


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order = Order.objects.create(
            user=validated_data['user'],
            product=validated_data['product'],
            confirmed=validated_data['confirmed'],
        )
        order.save()
        print(order.id)
        send_order_notification(order.id)
        return order
