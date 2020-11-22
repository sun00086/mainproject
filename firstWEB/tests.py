from bson import ObjectId
from django.test import TestCase


from firstWEB.models import MyDAO

mydao = MyDAO();


mydao.conn_user_mongodb()

condition = {'CURRENT': 'WEB001'}
newuser = {'$set':{'V_USER':'TRACY'}}

user = mydao.r_findUser('Kayla')
print(user)
mydao.conn_close()



