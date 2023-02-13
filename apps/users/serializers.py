from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.users.models import Education, Skills, WorkExperience

User = get_user_model()


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = (
            'id',
            'name',
        )


class ConnectionToSkillsSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Skills 
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        read_only_fields = ('owner',)
        fields = (
            'title',
            'description',
            'faculty',
            'start_date',
            'end_date',
            'graduated',
            'owner',
        )


class WorkExperienceSerializer(serializers.ModelSerializer):
    skills = ConnectionToSkillsSerializer(many=True, queryset=Skills.objects.all())

    class Meta:
        model = WorkExperience
        read_only_fields = ('owner',)
        fields = (
            'id',
            'job_title',
            'job_type',
            'company_name',
            'position',
            'location',
            'workplace_type',
            'currently_working',
            'start_date',
            'end_date',
            'description',
            'owner',
            'skills',
        )
    

class UserSerializer(serializers.ModelSerializer):
    user_work_exp = WorkExperienceSerializer(many=True, read_only=True)
    user_educattion = EducationSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'image',
            'phone_number',
            'bio',
            'user_work_exp',
            'user_educattion',
            'create_at',
        )


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'image',
            'bio',
            'phone_number',
            'create_at',
            'password',
        )

    def create(self, validated_data):
        password = validated_data['password']
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'image',
            'bio',
            'phone_number',
        )


class UserShowSerializer(serializers.ModelSerializer):
    user_work_exp = WorkExperienceSerializer(many=True, read_only=True)
    user_educattion = EducationSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'image',
            'bio',
            'user_work_exp',
            'user_educattion',
        )
        