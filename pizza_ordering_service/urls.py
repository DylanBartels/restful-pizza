from rest_framework.routers import SimpleRouter

from pizza_ordering_service.views import UserViewSet, OrderViewSet, PizzaViewSet

router = SimpleRouter()
router.register("users", UserViewSet)
router.register("orders", OrderViewSet)
router.register("pizzas", PizzaViewSet)

urlpatterns = router.urls
