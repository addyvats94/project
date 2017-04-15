from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse	
#from.forms import LoginForm,RegisterForm
from django.contrib.auth import logout

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication

from . import serializers, utils

# Create your views here.
def home(request):
	# form=LoginForm(request.POST or None)
	# context={'form':form}
	 data = {
	 	'title': 'Home',
	 	'name': 'ashu'
	 }
	 return render(request,'gallery.html', data)

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

class Login(APIView):
	"""
	"""
	authentication_classes = (CsrfExemptSessionAuthentication,)
	def get(self,request):
		"""login function"""

		return render(request,'user/login.html',{})
	
	def post(self, request):

		data = utils.login_user(request)
		return Response(data, status=status.HTTP_200_OK)


class Logout(APIView):
	""""""
	authentication_classes = (CsrfExemptSessionAuthentication,)
	def post(self, request):
		# status_code = utils.logout_user(request)
		logout(request)
		# if status_code:
		return Response({'message': 'logout successfully'}, status=status.HTTP_200_OK)
		# return Response({'message': 'some error occured'}, status=status.HTTP_400_BAD_REQUEST)


class UserSave(APIView):
	#form=RegisterForm(request.POST or None)
	#context={'form':form}
	authentication_classes = (CsrfExemptSessionAuthentication,)
	def get(self,request):
		return render(request,'user/register.html',{})
 	
 	def post(self, request):
 		
 		
	
 		data = request.data
 		user_data = {
 			'firstname': data.get('firstname'),
 			'lastname': data.get('lastname'),
 			'username': data.get('username'),
 			'mobile_no': data.get('mobile_no'),
 			'email': data.get('email'),
 			'roll_no': data.get('roll_no'),
 			'college': data.get('college'),
 			'password': data.get('password'),
 			

 		}
 		room_data = {
 			'room_type': data.get('room_type'),
 			'room_size': data.get('room_size')
 		}
 		user_serializer = serializers.UserSerializer(data=user_data)
 		try:
 			
			if user_serializer.is_valid():
				user = user_serializer.save() 
				user_room_serializer = serializers.UserPreferenceSerialzier(data=room_data)
				if user_room_serializer.is_valid():
					user_room_serializer.save(user=user)
					return Response({'message': 'success'}, status=status.HTTP_200_OK)
				return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			return Response({'message': 'error'}, status=status.HTTP_400_BAD_REQUEST)
		except:
			return Response({'message': 'error'}, status=status.HTTP_400_BAD_REQUEST)				
 			
	 	
	 	
	# @method_decorator(csrf_exempt)	
	# def dispatch(self, *args, **kwargs):
	# 	return super(UserSave, self).dispatch(*args, **kwargs)	
#def logout(request):
 #	return 	 	
