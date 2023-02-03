from rest_framework.routers import DefaultRouter

from apps.message.views import MessageApiViewSet


router = DefaultRouter()
router.register(
    prefix='',
    viewset=MessageApiViewSet,
    )

urlpatterns = router.urls
