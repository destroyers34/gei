from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def main_gpao(request):
    return render(request,"gpao/main_gpao.html")