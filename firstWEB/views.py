from django.shortcuts import render

# Create your views here.
from firstWEB.models import MyDAO
from datetime import date, datetime

mydao = MyDAO();

#today = datetime.strptime(date.today(),'%Y-%m-%d')
today = datetime.strftime(date.today(),'%Y-%m-%d')

def index(request):
    v_user = request.POST['v_user']

    user = {'USER': v_user, 'DATE': today}
    return render(request,'index.html',context={'user':user})

def login(request):
    return  render(request,'login.html')

def register(request):
    return  render(request,'register.html')

def register_done(request):
    v_user = request.POST['v_user']
    v_email = request.POST['v_email']
    v_password = request.POST['v_password']

    mydao.conn_user_mongodb()
    user = {'USER': v_user, 'EMAIL': v_email, 'PASSWORD': v_password}
    mydao.r_add(user)
    mydao.conn_close()
    return render(request, 'register_done.html')

def listAll(request):
     mydao.conn_info_mongodb()
     lst = mydao.r_displayAll()
     mydao.conn_close()
     return render(request, 'list_all.html',context={'list':lst})



def addnew(request):
    return render(request,'addnew.html')

def addnew_done(request):
    topic = request.POST['topic']
    v_title = request.POST['v_title']
    v_dec = request.POST['v_dec']
    v_link = request.POST['v_link']

    mydao.conn_info_mongodb()
    info = {'TOPIC': topic, 'TITLE': v_title, 'DEC': v_dec,'LINK':v_link,'DATE':today}
    mydao.r_add(info)
    mydao.conn_close()
    return render(request,'addnew_done.html')

def find(request):
    return render(request,'find.html')

def result(request):
    #record = mydao.r_displayByDate('2020-06-06')
    record = {'ID': '001', 'DATE': '2020-10-2', 'CASES': 1, 'DEATHS': 2, 'FR': 'NAME FR', 'EN': 'NAME EN'}
    return  render(request,'result.html',context={'data':record})