from django.urls import path, include
from rest_framework import routers
from apps.business.views import BusinessViewSet

router = routers.DefaultRouter()
router.register(r'businesses', BusinessViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
