from rest_framework.routers import DefaultRouter

from apps.contacts.views import ContactsAPIViewSet


router = DefaultRouter()
router.register(
    '',
    ContactsAPIViewSet,
    basename='contacts'
    )

urlpatterns = router.urls