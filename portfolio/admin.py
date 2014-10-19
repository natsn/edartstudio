from django.contrib import admin
from .models import Art, Portfolio

@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    pass

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass