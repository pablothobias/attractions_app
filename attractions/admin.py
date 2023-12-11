from django.contrib import admin
from .models import Attractions

@admin.register(Attractions)
class AttractionsAdmin(admin.ModelAdmin):
    ...
