from django.urls import path,include
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views
router = DefaultRouter()
router.register(r'users',views.UserAPIView)

urlpatterns=[
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('groups/', views.GroupAPIView.as_view()),
    path('groups/<int:pk>', views.GroupDetailAPIView.as_view()),
] +router.urls