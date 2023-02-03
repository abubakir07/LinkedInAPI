from django.contrib import admin

from apps.users.models import User, WorkExperience, Skills, Education


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'image'
    )


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'company_name',
        'position',
    )


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'level'
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'faculty',
        'graduated'
    )