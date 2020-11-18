from django.test import TestCase

# Create your tests here.
from firstWEB.models import MyDAO

mydao = MyDAO();
# mydao.conn_user_mongodb()
#
# user = {'USER': 'v_user1', 'EMAIL': 'v_email', 'PASSWORD': 'v_password','DATE':'2020-11-17'}
# mydao.r_add(user)
# mydao.conn_close()
#
#
#
# result = mydao.r_displayById('v_user11')
# print(result)

mydao.conn_info_mongodb()
lst = mydao.r_displayAll()
for i in lst:
    print(i)