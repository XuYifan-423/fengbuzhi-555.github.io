# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import F

from .models import Visits,Clicks

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")


def visit(request):
    visit = get_object_or_404(Visits,pk=1)
    visit.times = F('times') +1
    visit.save()
    response = HttpResponse("%d" % visit.times)
    response.status_code = 200
    return response

def click(request):
    click = get_object_or_404(Clicks, pk=1)
    click.times = F('times') + 1
    click.save()
    response = HttpResponse("%d" % click.times)
    response.status_code = 200
    return response