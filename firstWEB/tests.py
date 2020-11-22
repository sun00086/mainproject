from bson import ObjectId
from django.test import TestCase


from firstWEB.models import MyDAO

mydao = MyDAO();


mydao.conn_user_mongodb()

condition = {'CURRENT': 'WEB001','V_USER':'TRACY'}

result = mydao.r_findCurrentUser()

print(result)

mydao.conn_close()



