from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pizza_ordering_service import views

urlpatterns = [
    path('pizzas/', views.PizzaList.as_view(), name='PizzaList'),
    path('pizzas/<int:pk>/', views.PizzaDetail.as_view(), name='PizzaDetail'),
    path('orders/', views.OrderList.as_view(), name='OrderList'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='OrderDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
