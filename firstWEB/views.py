from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from firstWEB.models import MyDAO
from datetime import date, datetime, time

mydao = MyDAO()



today = datetime.strftime(date.today(),'%Y-%m-%d')



def index(request):

    mydao.conn_info_mongodb()
    lst = mydao.r_displayAll()
    mydao.conn_close()
    mydao.conn_user_mongodb()
    v_user = mydao.r_findCurrentUser()
    lst.append({'V_USER':v_user})
    mydao.conn_close()


    return render(request, 'index.html', context={'list': lst})

def login(request):

    name = 'abc'
    return  render(request,'login.html',context={'user': name})

def login_done(request):
    # v_user = request.POST['v_user']
    #
    # mydao.conn_user_mongodb()
    # v_user = mydao.r_findById(v_user)
    # if v_user == None:
    #     v_user = 'Did not find it.'
    # mydao.conn_close()
    return render(request, 'login_done.html')


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
    topic = request.POST['v_topic']
    v_title = request.POST['v_title']
    v_content = request.POST['v_content']
    v_sub_title = request.POST['v_sub_title']

    mydao.conn_info_mongodb()
    info = {'TOPIC': topic, 'TITLE': v_title, 'CONTENT': v_content,'SUBTITLE':v_sub_title,'DATE':today}
    mydao.r_add(info)
    mydao.conn_close()
    return render(request,'addnew_done.html')

def find(request):
    return render(request,'find.html')

def result(request):
    str =  request.POST['v_keywords']

    mydao.conn_info_mongodb()
    lst = mydao.r_findByKey({'$or': [{'TOPIC': {'$regex': '.*' + str + '.*', '$options': '$i'}},
                                        {'CONTENT': {'$regex': '.*' + str + '.*', '$options': '$i'}},
                                        {'SUBTITLE': {'$regex': '.*' + str + '.*', '$options': '$i'}},
                                        {'TITLE': {'$regex': '.*' + str + '.*', '$options': '$i'}}]})
    mydao.conn_close()
    return  render(request,'result.html',context={'data':lst})

def current_content(request):
    str = request.POST['v_id']

    mydao.conn_info_mongodb()
    lst = mydao.r_findById(str)
    mydao.conn_close()

    for rlt in lst:
        html = rlt['CONTENT']

    html = "<html><body>" + html + "</body></html>"
    return HttpResponse(html)


