from django.http import HttpResponse
from django.shortcuts import render_to_response
import urllib, urllib2
from django.utils import simplejson
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from timezoneaware.models import stats
from django.core import serializers
import datetime
from dateutil import tz
from pytz import UTC

from pytz import timezone, utc
from django.conf import settings
#@csrf_exempt
def index(request):
	list=stats.objects.order_by('-id')
	#tosend=serializers.serialize("json", list)
	latesttime=list[0].time
	now=datetime.datetime.now()
	TZ = timezone(settings.TIME_ZONE)
	now=TZ.localize(now.replace(microsecond=0)).astimezone(utc).replace(tzinfo=None).isoformat() + 'Z'
	return render_to_response('index.html',{ 'latesttime' : latesttime ,'currtime' : now }, context_instance=RequestContext(request))

def add(request):
	stat=stats()
	stat.save()
	list=stats.objects.order_by('-id')
	latesttime=list[0].time
	now=datetime.datetime.now()
	return render_to_response('add.html',{ 'latesttime' : latesttime ,'currtime' : now }, context_instance=RequestContext(request))