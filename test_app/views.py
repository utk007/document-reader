from django.shortcuts import render
from test_proj.new_celery import foo
from django.http import HttpResponse
# Create your views here.
def test_celery(request):
    """ method to test the celery jobs
    """
    print("starting background tasks")
    foo.delay()
    return HttpResponse('hey you !!!')
