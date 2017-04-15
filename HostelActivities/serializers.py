from . import models

from rest_framework import serializers

class RoomSerializer(serializers.ModelSerializer):
	""""""
	allocated_to = serializers.CharField(source='allocated_to.username')
	floor = serializers.CharField(source='get_floor_name')
	hostel = serializers.CharField(source='hostel.hostel_name')
	room_size=serializers.CharField(source='get_room_size')
	class Meta:
		model = models.Room
		exclude = ('id',)

