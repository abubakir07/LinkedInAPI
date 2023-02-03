from django.contrib import admin

from apps.favorites.models import Favorite


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'owner',
    )
