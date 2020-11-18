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



    def add(self):
        pass
    def delete(self):
        pass
    def update(self):
        pass


    def r_displeyAll(self):
        lst = []
        results = self.collection.find()
        for i in results:
            r1 = {'ID': i['ID'], 'DATE': i['DATE'], 'CASES': i['CASES'], 'DEATHS': i['DEATHS'], 'FR': i['NAME FR'], 'EN': i['NAME EN']}
            lst.append(r1)

        return lst

    def r_displayById(self, id):

        result = self.collection.find_one(({"USER": id}))
        if result == None:
            return None
        else:
            return result

    def r_add(self,newRecord):
        self.collection.insert_one(newRecord)
        print("save successful.")
