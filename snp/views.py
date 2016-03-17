from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.http import Http404
from django.template import RequestContext, loader
# Create your views here.

from django.http import HttpResponse
from .models import VCF,CSV
# Create your views here.

def index(request):
    return HttpResponse('index')