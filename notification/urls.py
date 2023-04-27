from django.urls import path, include
from notification import views

urlpatterns = [
    path('notification/', views.Notifications.as_view()),

]
