from django.urls import path, include
from user import views






from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', views.Users)


router.register('product', views.Products)
router.register('order', views.Orders)

urlpatterns = [
    path('', include(router.urls)),

]
