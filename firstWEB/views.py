from django.shortcuts import render

# Create your views here.
from firstWEB.models import MyDAO


def index(request):
    return render(request,'index.html')

def displayAll(request):
    mydao = MyDAO();
    mydao.conn_mongodb()
    allList = mydao.r_displeyAll()
    return  render(request,'resultlist.html',context={'list':allList})

def addnew(request):
    return render(request,'addnew.html')

def find(request):
    return render(request,'find.html')

def result(request):
    mydao = MyDAO();
    mydao.conn_mongodb()
    record = mydao.r_displayByDate('2020-06-06')
    return  render(request,'result.html',context={'data':record})