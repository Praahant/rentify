from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('property/create/', views.property_create, name='property_create'),
    path('property/list/', views.property_owned, name='property_owned'),
    path('property/<int:pk>/update/', views.property_update, name='property_update'),
    path('property/<int:pk>/delete/', views.property_delete, name='property_delete'),
    path('property/<int:pk>/detail/', views.property_seller_detail, name='seller_detail'),
]
