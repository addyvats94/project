from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.views import APIView, Response
from django.views.generic.base import TemplateView
from django.conf import settings
from django.http import HttpResponse

from userprofile import utils
from . import models, serializers

import os

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
		notices=models.Notices.objects.all()
		return render(request,'notice.html', {'data': notices})

class Aboutus(APIView):
	def get(self,request):
		return render(request,'aboutus.html',{})		


class GetDocument(TemplateView):
    """
    Get Document view
    """

    def get(self, request, path):
		"""
		returns document
		"""
		file_name, file_ext = os.path.splitext(path)
		file_name = path.split('/')[-1]
		path = settings.MEDIA_ROOT + file_name
		test_file = open(path, 'rb')
		response = HttpResponse(content=test_file)
		if file_ext == '.jpg':
			response['Content-Type'] = "image/jpg"
			response['Content-Disposition'] = 'attachment; filename="%s.jpg"' \
											  % file_name
		elif file_ext == '.pdf':
			response['Content-Type'] = 'application/pdf'
			response['Content-Disposition'] = 'attachment; filename="%s.pdf"' \
											  % file_name
		else:
			response['Content-Type'] = 'application/msword'
			response['Content-Disposition'] = 'attachment; filename="%s.doc"' \
											  % file_name
		return response
