from rest_framework.routers import DefaultRouter

from apps.posts.views import PostApiViewSet, UserContactPostView


router = DefaultRouter()
router.register(
    prefix="post",
    viewset=PostApiViewSet
)
router.register(
    prefix='contact-post',
    viewset=UserContactPostView
)

urlpatterns = router.urls
