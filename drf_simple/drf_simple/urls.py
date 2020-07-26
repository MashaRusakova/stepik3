from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from .views import beautybox_list, beautybox_content,\
    recipient_list, recipient_content


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product-sets/', beautybox_list, name='beautybox-list'),
    path('api/product-sets/<int:pk>/', beautybox_content, name='beautybox-content'),
    path('api/recipients/', recipient_list, name='recipient-list'),
    path('api/recipients/<int:pk>/', recipient_content, name='recipient-content'),
    path('api/product-sets/?min_price=N/', beautybox_list, name='product-price-min'),
    path('api/product-sets/?min_weight=N/', beautybox_list, name='product-weight-min'),
]
