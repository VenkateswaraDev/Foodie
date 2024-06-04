from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    data = ['Pizza','Bread','Pasta','Salad']
    context = {'foods':data}
    return render(request,'sandbox/index.html',context)