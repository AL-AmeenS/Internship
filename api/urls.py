from django.urls import include, path
from rest_framework import routers
from .views import CustomerView, ProductView

router = routers.DefaultRouter()
router.register(r'customers', CustomerView)
router.register(r'products', ProductView)

urlpatterns = [
    path('', include(router.urls)),
]