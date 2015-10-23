from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import NextMeeting

def index(request):
    next_meetings = NextMeeting.objects.order_by('-meeting_date')[:5]
    template = loader.get_template('meeting/index.html')
    context = RequestContext(request, {'meeting_date':next_meetings.reverse()[0].meeting_time})
    return HttpResponse(template.render(context))

