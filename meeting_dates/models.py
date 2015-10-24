from django.db import models

class NextMeeting(models.Model):
	meeting_date = models.DateField('meeting date')
	meeting_time = models.CharField(max_length=200)
	def __str__(self):
		return self.meeting_time

class Officers(models.Model):
	year = models.CharField(max_length=4)

	president = models.CharField(max_length=80)
	president_email = models.EmailField(default='youremail@rpi.edu')

	vice_president = models.CharField(max_length=80)
	vice_president_email = models.EmailField(default='youremail@rpi.edu')

	treasurer = models.CharField(max_length=80)
	treasurer_email = models.EmailField(default='youremail@rpi.edu')

	secretary = models.CharField(max_length=80)
	secretary_email = models.EmailField(default='youremail@rpi.edu')

	webmaster = models.CharField(max_length=80)
	webmaster_email = models.EmailField(default='youremail@rpi.edu')
	
	def __str__(self):
		return self.year
