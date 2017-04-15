from django.conf.urls import url
from . import views

urlpatterns=[
	     
	     
	     url(r'^register/create/$',views.UserSave.as_view(), name='register-create'),

	     url(r'^register/$',views.UserSave.as_view(), name='register-get'),
	     url(r'^login/$',views.Login.as_view(),name='login-get'),
		 url(r'^logout/$',views.Logout.as_view(),name='logout'),
	     #url(r'^register/$',views.register,name='register'),
	     url(r'^',views.home, name='home'),
]	
