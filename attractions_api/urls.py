from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from core.api.viewsets import AttractionViewSet

router = routers.DefaultRouter()
router.register(r'attractions', AttractionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
