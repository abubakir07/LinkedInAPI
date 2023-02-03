from rest_framework.routers import DefaultRouter
from .views import PostLikeViewSet, CommentLikeViewSet

router = DefaultRouter()
router.register(
    prefix="post-like",
    viewset=PostLikeViewSet
)
router.register(
    prefix="comment-like",
    viewset=CommentLikeViewSet
)

urlpatterns = router.urls