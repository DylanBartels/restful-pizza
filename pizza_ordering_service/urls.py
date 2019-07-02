from rest_framework.routers import SimpleRouter
from pizza_ordering_service.views import CustomerViewSet, OrderViewSet, PizzaViewSet


router = SimpleRouter()
router.register("customers", CustomerViewSet)
router.register("orders", OrderViewSet)
router.register("pizzas", PizzaViewSet)

urlpatterns = router.urls
