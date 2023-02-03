from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.users.models import Education, Skills, WorkExperience


User = get_user_model()


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    work_experience = WorkExperienceSerializer(many=True)
    education = EducationSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'image',
            'phone_number',
            'bio',
            'is_premium',
            'work_experience',
            'education',
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
            'is_premium',
            'password',
        )

    def create(self, validated_data):
        password = validated_data['password']
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    work_experience = WorkExperienceSerializer(many=True)
    education = EducationSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'image',
            'bio',
            'phone_number',
            'is_premium',
            'work_experience',
            'education',
            
        )