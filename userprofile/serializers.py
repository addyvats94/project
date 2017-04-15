from rest_framework import serializers
from .models import User, UserPreference

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		exclude = ('id',)

class UserPreferenceSerialzier(serializers.ModelSerializer):
	class Meta:
		model = UserPreference
		exclude = ('id',)