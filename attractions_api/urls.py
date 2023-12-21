from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from address.api.viewsets import AddressViewSet
from attractions_info.api.viewsets import AttractionInfoViewSet
from core.api.viewsets import AttractionViewSet
from reviews.api.viewsets import ReviewViewSet

router = routers.DefaultRouter()
router.register(r"attractions", AttractionViewSet)
router.register(r"attractionsinfo", AttractionInfoViewSet)
router.register(r"address", AddressViewSet)
router.register(r"reviews", ReviewViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
