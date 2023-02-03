from rest_framework.routers import DefaultRouter

from apps.chats.views import ChatAPIViewSet


router = DefaultRouter()
router.register(
    '',
    ChatAPIViewSet,
    basename='chats'
    )

urlpatterns = router.urls