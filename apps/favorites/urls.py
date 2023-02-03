from rest_framework.routers import DefaultRouter

from apps.favorites.views import FavoriteApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=FavoriteApiViewSet
)

urlpatterns = router.urls
