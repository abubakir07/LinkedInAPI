from rest_framework.routers import DefaultRouter

from apps.users.views import UserApiViewSet, SkillsAPIViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=UserApiViewSet
)
router.register(
    prefix="skills",
    viewset=SkillsAPIViewSet
)


urlpatterns = router.urls