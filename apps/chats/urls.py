from rest_framework.routers import DefaultRouter

from apps.chats.views import ChatApiViewSet


router = DefaultRouter()
router.register(
    '',
    ChatApiViewSet,
    basename='chats'
    )

urlpatterns = router.urls