from django.db import models

class NextMeeting(models.Model):
	meeting_date = models.DateTimeField('meeting date')
	meeting_time = models.CharField(max_length=200)
	def __str__(self):
		return self.meeting_time

class Officers(models.Model):
	president = models.CharField(max_length=200)
	vice_president = models.CharField(max_length=200)
	treasurer = models.CharField(max_length=200)
	secretary = models.CharField(max_length=200)
	webmaster = models.CharField(max_length=200)
	def __str__(self):
		return self.officer_text
