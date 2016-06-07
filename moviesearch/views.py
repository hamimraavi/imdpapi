from django.http import HttpResponse
import search
import pdb

def index(request):
    res = search.get_all_details("inception")
    return HttpResponse(res)

def results1(request, movie):
    res = search.get_all_details(movie)
    return HttpResponse(res)

# Create your views here.
