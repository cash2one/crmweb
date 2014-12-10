from django.shortcuts import render_to_response
from django.template import RequestContext

def scan(request):
	return render_to_response('scan.html',context_instance=RequestContext(request))
