from rest_framework import serializers,validators
from .models import Profile,Level,Department,College
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name')

        extra_kwargs = {
            "password":{"write_only":True},
            "email":{
                "required":True,
                "allow_blank":False,
                "validators":[
                    validators.UniqueValidator(
                        User.objects.all(), "A user with that email already exist"
                    )
                ]
            }
        }

    def create(self,validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        user = User.objects.create(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        return user

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('level', 'id')


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('college', 'id')

class DepartmentSerializer(serializers.ModelSerializer):
    college = CollegeSerializer()
    class Meta:
        model = Department
        fields = ('dept', 'id','college',)

class ProfileSerializer(serializers.ModelSerializer):
    level = LevelSerializer()
    dept = DepartmentSerializer()
    class Meta:
        model = Profile
        fields = ('id','img_profile', 'level', 'dept', 'teacher','staff','get_image',)

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','profile')


class UpdateProfileSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True, default= UserSerializer())
    class Meta:
        model = Profile
        fields = ('img_profile',)