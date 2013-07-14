from django.http import HttpResponse
from django.shortcuts import render_to_response
import urllib, urllib2
from django.utils import simplejson
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from timezoneaware.models import stats
from django.core import serializers
import datetime

#@csrf_exempt
def index(request):
	list=stats.objects.all()
	tosend=serializers.serialize("json", list)
	now=datetime.datetime.now()
	return render_to_response('index.html',{ 'data' : tosend ,'currtime' : now }, context_instance=RequestContext(request))