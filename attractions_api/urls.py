from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from core.api.viewsets import AttractionViewSet
from attractions_info.api.viewsets import AttractionInfoViewSet
from address.api.viewsets import AddressViewSet

router = routers.DefaultRouter()
router.register(r"attractions", AttractionViewSet)
router.register(r"attractionsinfo", AttractionInfoViewSet)
router.register(r"address", AddressViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
