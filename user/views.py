





from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated







from user.filters import ProductFilter
from user.models import User, Product, Order
from user.serializers import UserSerializer, ProductSerializer, OrderSerializer


# Create your views here.
class Users(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class Products(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    permission_classes = [IsAuthenticated]


class Orders(viewsets.ModelViewSet):
    queryset = Order.objects.all()





    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

