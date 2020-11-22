from bson import ObjectId
from django.shortcuts import render
from pymongo import MongoClient

# Create your models here.



class MyDAO(object):

    def conn_user_mongodb(self):
        self.cluster = MongoClient(
            "mongodb+srv://sun00086:yA549090@cluster0.vb0ks.mongodb.net/mydb?retryWrites=true&w=majority")
        self.db = self.cluster['mdb']
        self.collection = self.db['user']
        print("conn user table successful.")



    def conn_close(self):
        self.cluster.close()

    def conn_info_mongodb(self):
        self.cluster = MongoClient(
            "mongodb+srv://sun00086:yA549090@cluster0.vb0ks.mongodb.net/mydb?retryWrites=true&w=majority")
        self.db = self.cluster['mdb']
        self.collection = self.db['info']
        print("conn info table successful.")


    def r_displayAll(self):
        lst = []
        results = self.collection.find()
        for i in results:
            res = {'ID':i['_id'],'TOPIC': i['TOPIC'], 'TITLE': i['TITLE'], 'SUBTITLE': i['SUBTITLE'], 'CONTENT': i['CONTENT'], 'DATE': i['DATE']}
            lst.append(res)

        return lst

    def r_findByKey(self,lst):
        result = self.collection.find(lst)


        if result == None:
            return None
        else:
            lst = []
            for i in result:
                res = {'ID': i['_id'], 'TOPIC': i['TOPIC'], 'TITLE': i['TITLE'], 'SUBTITLE': i['SUBTITLE'],
                       'CONTENT': i['CONTENT'], 'DATE': i['DATE']}
                lst.append(res)
            return lst

    def r_findById(self, str):

        result = self.collection.find({'_id' : ObjectId(str)})
        if result == None:
            return None
        else:
            return result

    def r_findUser(self,v_user):
        result = self.collection.find({'USER': v_user})
        for u in result:
            return u['USER']

    def r_add(self,newRecord):
        self.collection.insert_one(newRecord)
        print("save successful.")

    def r_update(self,user):
        condition = {'CURRENT': 'WEB001'}
        newValues = {"$set": {"V_USER": user}}
        result = self.collection.update_one(condition,newValues)
        return result

    def r_findCurrentUser(self):
        condition = {'CURRENT': 'WEB001'}
        result = self.collection.find(condition)
        for u in result:
            return  u['V_USER']

