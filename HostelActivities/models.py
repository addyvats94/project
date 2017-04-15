from __future__ import unicode_literals

from django.db import models
from userprofile.models import User

# Create your models here.
class Hostel(models.Model):
	hostel_name=models.CharField(max_length=100,blank=False,null=True)
	rooms=models.IntegerField(blank=True,null=True)
	warden=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    	)
	
	def __unicode__(self):
		return self.hostel_name
	

class Notices(models.Model):
	notices=models.FileField(blank=True,null=True)

class Gallery(models.Model):
	photos=models.ImageField(blank=True,null=True)

class Room(models.Model):
	ZERO = '0'
	FIRST = '1'
	SECOND = '2'
	THIRD = '3'
	FOURTH = '4'
	FLOOR_CHOICES = (
    	(ZERO, "Ground Floor"),
    	(FIRST, "1st Floor"),
    	(SECOND, "2nd Floor"),
    	(THIRD, "3rd Floor"),
    	(FOURTH, "4th Floor"),
    	)
	ROOM_SIZE = (
	(FIRST, "Single Seater"),
	(SECOND, "Double Seater"),
	(THIRD, "Triple Seater"),
 	)
 	ROOM_TYPE = (
	("NON-AC", "NON-AC"),
	("AC", "AC"),
 	)

	room_no=models.IntegerField(blank=True,null=True)
	floor=models.CharField(max_length=15,choices=FLOOR_CHOICES,default=FIRST)
	allocated_to=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	hostel=models.ForeignKey(
	Hostel,
        on_delete=models.CASCADE,
	    )

	is_vacant=models.BooleanField(default=False)
	room_size=models.CharField(max_length=15,choices=ROOM_SIZE,default=FIRST)
	room_type=models.CharField(max_length=15,choices=ROOM_TYPE,default="NON_AC")

	def __unicode__(self):
		return str(self.room_no) + "-hostel:" + str(self.hostel)

	def get_floor_name(self):
		return self.FLOOR_CHOICES[int(self.floor)][1]

	def get_room_size(self):
		return self.ROOM_SIZE[int(self.room_size)-1][1]		