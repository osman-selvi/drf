from rest_framework import routers
from products import views

router = routers.SimpleRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)