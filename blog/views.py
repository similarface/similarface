from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
import datetime
import csv
# Create your views here.

def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def my_view(request):
    foo=True
    if foo:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>')

def sime_view(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer=csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response