from django.conf.urls import url
from . import views
urlpatterns=[
	     url(r'^room/$', views.Room.as_view(), name='Room'),
	     url(r'^about/$',views.Aboutus.as_view(),name='Aboutus'),
	     url(r'^notice/$',views.Notice.as_view(),name='notice'),
		 url(r'^(?P<path>.*)?', views.GetDocument.as_view()),
	     
]	
