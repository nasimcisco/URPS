import pymongo
import json
import random


class mydb:
        def insert2(self,request,filename,fakefilename):
                myclient = pymongo.MongoClient("mongodb://localhost:27017/")
                mydb = myclient["mydatabase"]
                mycol = mydb["studentdb"]
                mydict = { 'name': request.form['name'], 'roll' :request.form['roll'],'mobile':request.form['mobile'],'email':request.form['email'],'department':request.form['department'],'session':request.form['session'],'father':request.form['father'],'fathermobile':request.form['fathermobile'],'filename':filename,'fakefilename':fakefilename,'nid':request.form['nid'],'address':request.form['address']}
                x = mycol.insert_one(mydict)
                return('<h1>successfully uploaded in server</h1>')
        def insert2_teacher(self,request,filename,fakefilename):
                myclient = pymongo.MongoClient("mongodb://localhost:27017/")
                mydb = myclient["mydatabase"]
                mycol = mydb["teacherdb"]
                mydict = { 'available':True ,'name': request.form['name'], 'mobile':request.form['mobile'],'email':request.form['email'],'department':request.form['department'],'filename':filename,'fakefilename':fakefilename,'nid':request.form['nid'],'address':request.form['address'],'faculty':request.form['faculty'],'internal':'','external':'','tabulator':'','scrutinizer':'','decoder':''}
                x = mycol.insert_one(mydict)
                return('<h1>successfully uploaded in server</h1>')
        def insert(self,request,filename,fakefilename,user):
                myclient = pymongo.MongoClient("mongodb://localhost:27017/")
                mydb = myclient["mydatabase"]
                mycol = mydb["elearning"]
                mydict = { request.form['department']: request.form['semester'], 'year': request.form['year'],'course':request.form['course'] ,'filename':filename,'fakefilename':fakefilename,'user':user}
                x = mycol.insert_one(mydict)
                return('<h1>successfully uploaded in server</h1>')
        def insert_dcourse(self,request) :
                myclient = pymongo.MongoClient("mongodb://localhost:27017/")
                mydb = myclient["mydatabase"]
                mycol = mydb["dcourse"]
                mydict = { 'course' :request.form['course'],'coursecode':request.form['coursecode'],'session':request.form['session'],'department':request.form['department'],'credit':request.form['credit'],'internal':request.form['internal'],'internalemail':request.form['internalemail'],'external':request.form['external'],'externalemail':request.form['externalemail'],'tabulator':request.form['tabulator'],'tabulatoremail':request.form['tabulatoremail'],'scrutinizer':request.form['scrutinizer'],'scrutinizeremail':request.form['scrutinizeremail'],'decoder':request.form['decoder'],'decoderemail':request.form['decoderemail'],'authority':request.form['authority']}
                x = mycol.insert_one(mydict)
                return('<h1>successfully uploaded in server</h1>')
        def t_universal_insert(self,d) :
                myclient = pymongo.MongoClient("mongodb://localhost:27017/")
                mydb = myclient["mydatabase"]
                mycol = mydb["resultdb"]
                mydict = d
                x = mycol.insert_one(mydict)
                return('<h1>successfully uploaded in server</h1>')
        def get(self,mydata):
                myclient = pymongo.MongoClient("mongodb://localhost:27017/")
                mydb = myclient["mydatabase"]
                mycol = mydb["studentdb"]
                myquery = mydata
                mydoc = mycol.find(myquery).sort("roll",-1)
                ls = []
                for x in mydoc:
                    ls.append(x)
                return ls

        def get_teacher(self,mydata):
                myclient = pymongo.MongoClient("mongodb://localhost:27017/")
                mydb = myclient["mydatabase"]
                mycol = mydb["teacherdb"]
                myquery = mydata
                mydoc = mycol.find(myquery)
                ls = []
                for x in mydoc:
                    ls.append(x)
                return ls
        def get_student(self,mydata):
                myclient = pymongo.MongoClient("mongodb://localhost:27017/")
                mydb = myclient["mydatabase"]
                mycol = mydb["studentdb"]
                myquery = mydata
                mydoc = mycol.find(myquery)
                ls = []
                for x in mydoc:
                    ls.append(x)
                return ls
        def get_dcourse(self,mydata):
                myclient = pymongo.MongoClient("mongodb://localhost:27017/")
                mydb = myclient["mydatabase"]
                mycol = mydb["dcourse"]
                myquery = mydata
                mydoc = mycol.find(myquery)
                ls = []
                for x in mydoc:
                    ls.append(x)
                return ls

        def check(self,request):
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydatabase"]
            mycol = mydb["user"]
            myquery = {'email' : request.form['email'],'password':request.form['password']}
            mydoc = mycol.find(myquery)
            ls = []
            for x in mydoc:
                ls.append(x)
            return ls
        def getcourse(self,coursequery):
             myclient = pymongo.MongoClient("mongodb://localhost:27017/")
             mydb = myclient["mydatabase"]
             mycol = mydb["elearning"]
             myquery = coursequery
             mydoc = mycol.find(myquery)
             ls = []
             for x in mydoc:
                ls.append(x)
             return ls
        def getusercourse(self,getusercoursequery):
             myclient = pymongo.MongoClient("mongodb://localhost:27017/")
             mydb = myclient["mydatabase"]
             mycol = mydb["course"]
             myquery = getusercoursequery
             mydoc = mycol.find(myquery)
             ls = []
             for x in mydoc:
                ls.append(x)
             return ls

        def getuserfilelist(self,editquery):
             myclient = pymongo.MongoClient("mongodb://localhost:27017/")
             mydb = myclient["mydatabase"]
             mycol = mydb["elearning"]
             myquery = editquery
             mydoc = mycol.find(myquery)
             ls = []
             for x in mydoc:
                ls.append(x)
             return ls
        def delete(self,roll):
             myclient = pymongo.MongoClient("mongodb://localhost:27017/")
             mydb = myclient["mydatabase"]
             mycol = mydb["studentdb"]
             myquery = {'roll' : roll }
             mycol.delete_one(myquery)
             return('<h1>successfully deleted in server</h1>')
        def delete_teacher(self,email):
             myclient = pymongo.MongoClient("mongodb://localhost:27017/")
             mydb = myclient["mydatabase"]
             mycol = mydb["teacherdb"]
             myquery = {'email' : email }
             mycol.delete_one(myquery)
             return('<h1>successfully deleted in server</h1>')
        def duplicate(self,roll):
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydatabase"]
            mycol = mydb["studentdb"]
            myquery = {'roll':roll}
            mydoc = mycol.find(myquery)
            ls = []
            for x in mydoc:
                ls.append(x)
            return ls
        def duplicate_dcourse(self,coursecode):
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydatabase"]
            mycol = mydb["dcourse"]
            myquery = {'coursecode':coursecode}
            mydoc = mycol.find(myquery)
            ls = []
            for x in mydoc:
                ls.append(x)
            return ls
        def delete_dcourse(self,coursecode):
             myclient = pymongo.MongoClient("mongodb://localhost:27017/")
             mydb = myclient["mydatabase"]
             mycol = mydb["dcourse"]
             myquery = {'coursecode' : coursecode }
             mycol.delete_one(myquery)
             return('<h1>successfully deleted in server</h1>')

        def duplicate_teacher(self,email):
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydatabase"]
            mycol = mydb["teacherdb"]
            myquery = {'email':email }
            mydoc = mycol.find(myquery)
            ls = []
            for x in mydoc:
                ls.append(x)
            return ls
        def passwd(self,mydata):
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydatabase"]
            mycol = mydb["studentdb"]
            myquery = mydata
            genpass = str(random.randint(100000,1000000))
            newvalues = { "$set": { "password": genpass } }
            mycol.update_one(myquery, newvalues)
            return ('successfully')
        def passwd_teacher(self,mydata):
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydatabase"]
            mycol = mydb["teacherdb"]
            myquery = mydata
            genpass = str(random.randint(100000,1000000))
            newvalues = { "$set": { "password": genpass } }
            mycol.update_one(myquery, newvalues)
            return ('successfully')
        def update_dcourse(self,k,e,c):
            mydata = { 'email' : e}
            l = self.get_teacher(mydata)
            ll = []
            if len(l[0][k]) > 0:
            	for i in l[0][k] :
            		if i == c :
            			return ('duplicate found !!')
            			
            		ll.append(i)
            ll.append(c)
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydatabase"]
            mycol = mydb["teacherdb"]
            myquery = mydata
            newvalues = { "$set": { k: ll } }
            mycol.update_one(myquery, newvalues)
            return ('successfully')
        def insert_secrets(self,mydata):
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydatabase"]
            mycol = mydb["secrets"]
            mydict = mydata
            x = mycol.insert_one(mydict)
            return ('successfully')
        def get_secrets(self,coursecode):
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydatabase"]
            mycol = mydb["secrets"]
            mydata ={'coursecode' : coursecode}
            myquery = mydata
            mydoc = mycol.find(myquery)
            ls = []
            for x in mydoc:
                ls.append(x)
            return ls
        def get_result(self,mydata):
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydatabase"]
            mycol = mydb["resultdb"]
            myquery = mydata
            mydoc = mycol.find(myquery)
            ls = []
            for x in mydoc:
                ls.append(x)
            return ls
        def insert_final_result(self,mydata):
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydatabase"]
            mycol = mydb["final_result"]
            mydict = mydata
            x = mycol.insert_one(mydict)
            return ('successfully')

        def get_final_result(self,mydata):
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydatabase"]
            mycol = mydb["final_result"]
            myquery = mydata
            mydoc = mycol.find(myquery)
            ls = []
            for x in mydoc:
                ls.append(x)
            return ls
        def insert_at_mid(self,d):
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydatabase"]
            mycol = mydb["at_mid"]
            mydict = d
            x = mycol.insert_one(mydict)
            return ('successfully')