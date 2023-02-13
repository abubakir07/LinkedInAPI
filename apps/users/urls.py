from rest_framework.routers import DefaultRouter

from apps.users.views import UserApiViewSet, UserShowApiViewSet, SkillsApiViewSet, WorkExperienceApiViewSet, EducationApiViewSet


router = DefaultRouter()
router.register(
    prefix="user",
    viewset=UserApiViewSet
)
router.register(
    prefix="user-info",
    viewset=UserShowApiViewSet
)
router.register(
    prefix="skills",
    viewset=SkillsApiViewSet
)
router.register(
    prefix="work_exp",
    viewset=WorkExperienceApiViewSet
)
router.register(
    prefix="education",
    viewset=EducationApiViewSet
)

urlpatterns = router.urls