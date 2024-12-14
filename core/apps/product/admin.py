from django.contrib import admin

from core.apps.product.models import YouModel

@admin.register(YouModel)
class YouModelAdmin(admin.ModelAdmin):
    pass
