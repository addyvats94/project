from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView, Response

from userprofile import utils
from . import models, serializers


# Create your views here.
# def login(request):
# 	form=LoginForm(request.POST or None)
# 	context={'form':form}
# 	return render(request,'index.html',context)

# def register(request):
# 	form=RegisterForm(request.POST or None)
# 	context={'form':form}
# 	return render(request,'HostelActivities/login.html',context)
 
class Room(APIView):
	"""
	"""
	def get(self,request):
		""""""
		rooms = models.Room.objects.all()
		serializer = serializers.RoomSerializer(rooms, many=True)

		if serializer.is_valid:
			return render(request,'hostel/room.html',{'data': serializer.data})
		return render(request,'hostel/room.html',{})

class Notice(APIView):
	"""
	"""
	def get(self,request):
		notice=models.Notices.objects.all()
		
		return render(request,'notice.html',{})

class Aboutus(APIView):
	def get(self,request):
		return render(request,'aboutus.html',{})		
