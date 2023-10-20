from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import DentalProfile

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = '__all__'
		
	def create(self, data):
		user_obj = UserModel.objects.create_user(email=data['email'], password=data['password'])
		user_obj.username = data['username']
		user_obj.save()
		return user_obj

class UserLoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField()

	def check_user(self, data):
		user = authenticate(username=data['email'], password=data['password'])
		if not user:
			raise ValidationError('User not found')
		return user

class DentalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DentalProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	dental_profiles = DentalProfileSerializer(many=True, read_only=True)
	
	class Meta:
		model = UserModel
		fields = ('email', 'username', 'dental_profiles')
		