from rest_framework.routers import DefaultRouter

from apps.posts.views import PostApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=PostApiViewSet
)

urlpatterns = router.urls
