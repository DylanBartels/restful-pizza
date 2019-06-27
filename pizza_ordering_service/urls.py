from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pizza_ordering_service import views

urlpatterns = [
    path('pizzas/', views.PizzaList.as_view()),
    path('pizzas/<int:pk>/', views.PizzaDetail.as_view()),
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:pk>/', views.OrderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
