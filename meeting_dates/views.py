from django.shortcuts import render,render_to_response

from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import NextMeeting, Officers

def index(request):
    next_meetings = NextMeeting.objects.order_by('-meeting_date')[:5]
    officers = Officers.objects.order_by('-president')
    template = loader.get_template('meeting/index.html')
    context = {
    	'meeting_time':next_meetings.reverse()[0].meeting_time,
    	'meeting_date':next_meetings.reverse()[0].meeting_date,
    	'president':officers[0].president,
    	'vice_president':officers[0].vice_president,
    	'treasurer':officers[0].treasurer,
    	'secretary':officers[0].secretary,
    	'webmaster':officers[0].webmaster,
    	'president_email':officers[0].president_email,
    	'vice_president_email':officers[0].vice_president_email,
    	'treasurer_email':officers[0].treasurer_email,
    	'secretary_email':officers[0].secretary_email,
    	'webmaster_email':officers[0].webmaster_email,
    }
    return render_to_response('index.html', context)