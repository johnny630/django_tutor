from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('http tutor index')

def special_case_2003(request):
    return HttpResponse('special_case_2003')

def year_archive(request, year):
    return HttpResponse(f'year_archive {year}')

def month_archive(request, year, month):
    return HttpResponse(f'month_archive {year}/ {month}')

def article_detail(request, year, month, slug):
    return HttpResponse(f'month_archive {year}/ {month}: slug: {slug}')