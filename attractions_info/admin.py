from django.contrib import admin
from .models import AttractionsInfo

# Register your models here.
@admin.register(AttractionsInfo)
class AttractionsInfoAdmin(admin.ModelAdmin):
    ...