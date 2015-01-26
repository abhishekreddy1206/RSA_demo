from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.
def index(request):
	return render_to_response("registration/index.html",context_instance=RequestContext(request))

def confirm(request):
	return render_to_response("registration/confirm.html",context_instance=RequestContext(request))

