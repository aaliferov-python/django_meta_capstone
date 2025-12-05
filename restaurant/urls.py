from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')

routerTables = routers.DefaultRouter()
routerTables.register(r'tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()), 
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()), 
    path('booking/', include(routerTables.urls), name='booking'),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]