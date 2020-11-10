from django.test import TestCase

# Create your tests here.
from firstWEB.models import MyDAO

mydao = MyDAO();
mydao.conn_mongodb()
lst = mydao.r_displayByDate('2020-06-06')
print(lst)