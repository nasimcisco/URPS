from flask import Flask, render_template,request,make_response,session,redirect,g
from mydb import mydb
from werkzeug import secure_filename
import mymail,json
import os ,random
from zeep import Client

test = mydb()
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n/'
@app.route('/')
def r_index():
   if g.email == 'registrar@cvasu.ac.bd':
      return render_template('r_index.html')
   else :
      return render_template('login.html')
@app.route('/r_reg')
def r_reg():
	if g.email == 'registrar@cvasu.ac.bd' :
	   return render_template('r_reg.html')
	else :
		return render_template('login.html')
@app.route('/r_reg_teacher')
def r_reg_teacher():
    if g.email == 'registrar@cvasu.ac.bd':
       return render_template('r_reg_teacher.html')
    else : 
    	return render_template('login.html')
@app.route('/r_alldata',methods = ['POST', 'GET'])
def r_alldata():
   if g.email == 'registrar@cvasu.ac.bd':
      if request.method == 'POST':
           l=test.duplicate(request.form['roll'])
           if len(l) > 0 :
              test.delete(request.form['roll']) 
           f = request.files['file']
           UPLOAD_FOLDER = 'C:/Users/nasim/Desktop/RPS/static'
           app.config['UPLOAD_FOLDER'] =UPLOAD_FOLDER
           f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
           filename = f.filename
           fakefilename = request.form['roll']
           s = test.insert2(request, filename, fakefilename)
           mydata = { 'session' :'2018' } 
           l = test.get(mydata)
           return render_template('r_alldata.html',l=l)
      else :
           mydata = { 'session' :'2018' } 
           l = test.get(mydata)
           return render_template('r_alldata.html',l=l) 
   else :
      return render_template('login.html')


@app.route('/r_alldata_teacher',methods = ['POST', 'GET'])
def r_alldata_teacher():
   if g.email == 'registrar@cvasu.ac.bd':
      if request.method == 'POST':
           l=test.duplicate_teacher(request.form['email'])
           if len(l) > 0 :
              test.delete_teacher(request.form['email']) 
           f = request.files['file']
           UPLOAD_FOLDER = 'C:/Users/nasim/Desktop/RPS/static'
           app.config['UPLOAD_FOLDER'] =UPLOAD_FOLDER
           f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
           filename = f.filename
           fakefilename = request.form['email']
           s = test.insert2_teacher(request, filename, fakefilename)
           mydata = { 'available' :True } 
           l = test.get_teacher(mydata)
           return render_template('r_alldata_teacher.html',l=l)
      else :
           mydata = { 'available' :True } 
           l = test.get_teacher(mydata)
           return render_template('r_alldata_teacher.html',l=l) 
   else :
   	   return render_template('login.html')
@app.route('/<roll>')
def r_r_view(roll):
	mydata = {'roll':roll}
	l =test.get(mydata)
	return render_template('r_view.html',l=l)
@app.route('/r_edit/<roll>')
def r_edit(roll):
	mydata = {'roll':roll}
	l =test.get(mydata)
	return render_template('r_edit.html',l=l)	
@app.route('/del/<roll>')
def delete(roll):
      s =test.delete(roll)
      return redirect('/r_alldata')
@app.route('/mail/<roll>') 
def mail(roll):
	mydata = {'roll' : roll}
	lp = test.passwd(mydata)
	l = test.get(mydata)
	recepient=l[0]['email']
	dict=l[0]
	mydict = {}
	for k, v in dict.items():
	    if k  == '_id' or k == 'fakefilename':
	    	continue
	    elif k == 'passwd' :
	    	mydict[k] = str(v)
	    else :
	    	mydict[k] = v
	mymail.send_email(recepient, mydict)
	return redirect('/r_alldata')
@app.route('/sms/<roll>')
def sms(roll):
      mydata ={ 'roll' :roll}
      lp = test.passwd(mydata)
      l = test.get(mydata)
         
      for result in l :
               
         sms_text = 'login url :ciis.cvasu.ac.bd' + '\n' + 'userid: ' + result['roll'] +'\n' +'password: ' + result['passwd'] +'\n'
         sms_phone = result['mobile']
         url = 'https://api2.onnorokomsms.com/sendsms.asmx?WSDL'
         client = Client(url)
         userName = '01991953330'
         password = '546c38'
         recipientNumber = sms_phone
         smsText = sms_text
         smsType = 'TEXT'
         maskName = ''
         campaignName = ''
         client.service.OneToOne(userName,password,recipientNumber,smsText,smsType,maskName,campaignName)
@app.route('/pass/<roll>')
def passwd(roll):
    mydata = {'roll' : roll}
    l = test.passwd(mydata)
    return redirect('/r_alldata')




@app.route('/show/<email>')
def r_view_teacher(email):
	mydata = {'email':email}
	l =test.get_teacher(mydata)
	return render_template('r_view_teacher.html',l=l)

@app.route('/r_edit_teacher/<email>')
def r_edit_teacher(email):
	mydata = {'email':email}
	l =test.get_teacher(mydata)
	return render_template('r_edit_teacher.html',l=l)	
@app.route('/del_teacher/<email>')
def delete_teacher(email):
      s =test.delete_teacher(email)
      return redirect('/r_alldata_teacher')
@app.route('/mail_teacher/<email>') 
def mail_teacher(email):
	mydata = {'email' : email}
	lp = test.passwd_teacher(mydata)
	l = test.get_teacher(mydata)
	recepient=l[0]['email']
	dict=l[0]
	mydict = {}
	for k, v in dict.items():
	    if k  == '_id' or k == 'fakefilename' or k == 'available':
	    	continue
	    elif k == 'passwd' :
	    	mydict[k] = str(v)
	    else :
	    	mydict[k] = v
	mymail.send_email(recepient, mydict)
	return redirect('/r_alldata_teacher')
@app.route('/sms_teacher/<email>')
def sms_teacher(email):
      mydata ={ 'email' :email}
      lp = test.passwd_teacher(mydata)
      l = test.get_teacher(mydata)
         
      for result in l :
               
         sms_text = 'login url :ciis.cvasu.ac.bd' + '\n' + 'userid: ' + result['email'] +'\n' +'password: ' + result['passwd'] +'\n'
         sms_phone = result['mobile']
         url = 'https://api2.onnorokomsms.com/sendsms.asmx?WSDL'
         client = Client(url)
         userName = '01991953330'
         password = '546c38'
         recipientNumber = sms_phone
         smsText = sms_text
         smsType = 'TEXT'
         maskName = ''
         campaignName = ''
         client.service.OneToOne(userName,password,recipientNumber,smsText,smsType,maskName,campaignName)
@app.route('/pass_teacher/<email>')
def passwd_teacher(email):
    mydata = {'email' : email}
    l = test.passwd_teacher(mydata)
    return redirect('/r_alldata_teacher')
@app.route('/d_index')
def d_index():
	if g.email == 'dean@cvasu.ac.bd' :
		return render_template('d_index.html')
	else :
		return render_template('login.html')



@app.route('/d_reg',methods=['POST','GET'])
def d_reg():
    if g.email == 'dean@cvasu.ac.bd':
         if request.method == 'POST' :
            ld = test.duplicate_dcourse(request.form['coursecode'])
            if len(ld) > 0 :
               s = test.delete_dcourse(request.form['coursecode'])
            s =test.insert_dcourse(request)
            s = test.update_dcourse('internal',request.form['internalemail'],request.form['coursecode'])
            s = test.update_dcourse('external',request.form['externalemail'],request.form['coursecode'])
            s = test.update_dcourse('tabulator',request.form['tabulatoremail'],request.form['coursecode'])
            s = test.update_dcourse('scrutinizer',request.form['scrutinizeremail'],request.form['coursecode'])
            s = test.update_dcourse('decoder',request.form['decoderemail'],request.form['coursecode'])
            mydata = { 'session' : '2018'}
            l = test.get_dcourse(mydata)
            return render_template('/d_alldata.html',l=l)
         else :
            mydata = {'available' : True}
            l = test.get_teacher(mydata)
            ll = []
            lll = []
            s = set()
            for j in l :
               ll.append(j['name'])
               lll.append(j['email'])
               s.add(j['department'])
            
            return render_template('d_reg.html',l=l,ll=ll,lll=lll,s=s)
    else :
      return render_template('login.html')
@app.route('/d_alldata')
def d_alldata():
	mydata = { 'session' : '2018'}
	l = test.get_dcourse(mydata)
	return render_template('d_alldata.html',l=l)
@app.route('/d_edit/<coursecode>')
def d_edit(coursecode):
      mydata = {'coursecode' : coursecode }
      ls=test.get_dcourse(mydata)
      mydata = {'available' : True}
      l = test.get_teacher(mydata)
      ll = []
      lll = []
      s = set()
      for j in l :
         ll.append(j['name'])
         lll.append(j['email'])
         s.add(j['department'])
      return render_template('d_edit.html',l=l,ll=ll,lll=lll,ls=ls,s=s)
@app.route('/t_index')
def t_index():
   if g.email :
      mydata = {'email' : g.email }
      l = test.get_teacher(mydata)
      return render_template('t_index.html',l=l)
   else :
   	return render_template('login.html')
@app.route('/t_universal/<role>')
def t_universal(role):
      if g.email :
         mydata = {'email' : g.email }
         l = test.get_teacher(mydata)
         return render_template('t_universal.html',l=l,role=role)
      else :
         return render_template('login.html')
@app.route('/d_secrets/<coursecode>')
def d_secrets(coursecode):
    
    l = test.get_secrets(coursecode)
    if len(l) > 0:
      return render_template('d_secrets.html',l=l) 
    else :
      mydata = {'session':'2018'}
      l = test.get(mydata)
      ll = {}
      ll['coursecode'] = coursecode
      for i in l :
          ll[i['roll']]=str(random.randint(1000,10000))

      s = test.insert_secrets(ll)
      l = test.get_secrets(coursecode)
    return render_template('d_secrets.html',l=l) 
@app.route('/t_universal_view/<coursecode>/<role>')
def t_universal_view(coursecode,role):
    l = test.get_secrets(coursecode)
    
    # for k,v in l[0].items() :
    # 	if k != '_id' and k != 'coursecode':
    # 		ll.append(v)
    # lll =[]
    # for _ in range(len(ll)):
    #    y = random.choice(ll)
    #    ll.remove(y)
    #    lll.append(y)
    d ={}
    for k,v in l[0].items():
        if k !='_id' and k!='coursecode':
            d[k] = v
    lll =  list(d.values())
    random.shuffle(lll)
    return render_template('t_universal_view.html',lll=lll,role=role,coursecode=coursecode)
    
@app.route('/t_universal_insert/<coursecode>/<role>' ,methods =['POST','GET'])
def t_universal_insert(coursecode,role):
         if request.method =='POST' :
            d ={}
            f = request.form
            for key in sorted(f.keys()):
              for value in f.getlist(key):
                  d[key] = value
            l = test.get_secrets(coursecode)
            d1 ={}
            for k1,v1 in l[0].items():
                if k1 !='_id' and k1!='coursecode':
                    d1[k1] = v1
            d3 = {}
            for k3,v3 in d1.items():
                for k4 ,v4 in d.items():
                    if v3 == k4 :
                        d3[k3] = v4
                        break
            d3['coursecode'] = coursecode
            d3['role'] = role
            s = test.t_universal_insert(d3)
         return redirect ('/t_index')
@app.route('/login',methods =['POST','GET'])
def login():
      if request.method == 'POST' :
         if request.form['role'] == 'registrar' or request.form['role'] =='dean' :
            l =test.check(request)
            if len(l) > 0 :
               if request.form['role'] == 'registrar':
                  session['email'] = request.form['email']
                  return redirect('/')
               else :
                  session['email'] = request.form['email']
                  return redirect('/d_index')

         elif request.form['role'] == 'teacher' :
               mydata = {'email' : request.form['email'] , 'password':request.form['password']}
               l = test.get_teacher(mydata)
               if len(l) > 0:
                  session['email'] = request.form['email']
                  return redirect('/t_index')
               else :
                  session.clear()
                  return render_template('login.html')

         elif request.form['role'] == 'student' :
         	mydata = {'email': request.form['email'],'password':request.form['password'] }
         	l = test.get_student(mydata)
         	if len(l) > 0:
         		session['email'] = request.form['email']
         		return redirect('/s_index')
      else :
         session.clear()
         return render_template('login.html')
@app.before_request
def before_request():
    g.email = None
    if 'email' in session:
        g.email = session['email']
@app.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')
@app.route('/s_index')
def s_index():
      if g.email :
         mydata = {'email' : g.email }
         l = test.get_student(mydata)
         return render_template('s_index.html',l=l)
      else :
         return render_template('login.html')	
@app.route('/s_admit')
def s_admit():
      if g.email :
         mydata ={'email' :g.email}
         l=test.get_student(mydata)
         return render_template('s_admit.html',l=l)
@app.route('/d_result/<coursecode>')
def d_result(coursecode):
    if g.email == 'dean@cvasu.ac.bd' :
       li =[]
       le =[]
       lt =[]
       ls =[]
       ld =[]
       lr =[]
       lsc =[]
       mydata = {'role' : 'internal' ,'coursecode' :coursecode }
       l1 = test.get_result(mydata)
       for k1,v1 in l1[0].items():
       		if k1 !='_id' and k1!='role' and k1!='coursecode':
       			li.append(v1)
       mydata = {'role' : 'external' ,'coursecode' :coursecode }
       l2 = test.get_result(mydata)
       for k2,v2 in l2[0].items():
       		if k2 !='_id' and k2!='role' and k2!='coursecode':
       			le.append(v2)
       mydata = {'role' : 'tabulator' ,'coursecode' :coursecode }
       l3 = test.get_result(mydata)
       for k3,v3 in l3[0].items():
       		if k3 !='_id' and k3!='role' and k3!='coursecode':
       			lt.append(v3)
       mydata = {'role' : 'scrutinizer' ,'coursecode' :coursecode }
       l4 = test.get_result(mydata)
       for k4,v4 in l4[0].items():
       		if k4 !='_id' and k4!='role' and k4!='coursecode':
       			ls.append(v4)
       mydata = {'role' : 'decoder' ,'coursecode' :coursecode }
       l5 = test.get_result(mydata)
       for k5,v5 in l5[0].items():
       		if k5 !='_id' and k5!='role' and k5!='coursecode':
       			ld.append(v5)
       l6 = test.get_secrets(coursecode)
       for k6,v6 in l6[0].items():
       		if k6 !='_id' and k6!='coursecode':
       			lr.append(k6)
       			lsc.append(v6)
    return render_template('d_result.html',li=li,le=le,lt=lt,ls=ls,ld=ld,lr=lr,lsc=lsc)

@app.route('/d_marksheet')
def d_marksheet():
	if g.email == 'dean@cvasu.ac.bd':
	   mydata = {'session' : '2018'}
	   l = test.get_dcourse(mydata)
	   return render_template('d_marksheet.html',l=l)
@app.route('/d_secretsgen')
def d_secretsgen():
	if g.email == 'dean@cvasu.ac.bd':
	   mydata = {'session':'2018'}
	   l = test.get_dcourse(mydata)
	   return render_template('d_secretsgen.html',l=l)

@app.route('/d_final_result')
def d_final_result():
      if g.email :
         mydata = { 'email' :g.email }
         l = test.get_final_result(mydata)
         if len(l) > 0 :
            return redirect ('/s_final_result')
         else :
            mydata = {'session' : '2018'}
            lt = test.get_dcourse(mydata)
            for i in range(len(lt)):
                d ={}
                mydata = {'email' :g.email}
                l = test.get_student(mydata)
                for k,v in l[0].items():
                        if k == 'name' or k =='roll' or k=='session' or k=='email':
                                d[k]=v
                mydata = {'session' : '2018'}
                l = test.get_dcourse(mydata)
                for k,v in l[i].items():
                        if k == 'course' or k == 'coursecode' or k =='credit' :
                                d[k] = v
                l = test.get_secrets(d['coursecode'])
                for k,v in l[0].items():
                        if k == d['roll'] :
                                d['secrets'] = v
                                break
                mydata = {'role' : 'internal' ,'coursecode': d['coursecode']}
                l = test.get_result(mydata)
                for k,v in l[0].items():
                        if k == d['secrets']:
                                d['marks'] = v
                                break 
                d['grade'] = find_grade(int(d['marks']))
                d['point'] = find_point(int(d['marks']))
                s = test.insert_final_result(d)
            return redirect ('/s_final_result')




def find_grade(marks):
      if marks >=80:
         return ("A+")
      elif marks >=70:
         return("A")
      elif marks >=60:
         return ("B+")
      elif marks >=50:
         return ("B")
      else:
         return ("C")

def find_point(marks):
      if marks >=80:
         return ("4.0")
      elif marks >=70:
         return("3.5")
      elif marks >=60:
         return ("3.0")
      elif marks >=50:
         return ("2.5")
      else:
         return ("2")

@app.route('/s_final_result')
def s_final_result():
      if g.email :
         d ={}
         sum =0
         sum1 =0
         mydata = {'email' :g.email}
         l = test.get_student(mydata)
         for k,v in l[0].items():
            if k == 'name' or k =='roll' or k=='session' :
                d[k]=v
         mydata = {'roll' :d['roll']}
         l = test.get_final_result(mydata)
         for result in l:
                sum += float(result['point'])*float(result['credit'])
                sum1 += float(result['credit'])

         sum2 = sum/sum1
         return render_template('s_final_result.html',l=l,sum1=sum1,sum2=sum2,d=d)
@app.route('/t_at_mid/<coursecode>',methods = ['POST','GET'])
def t_at_mid(coursecode):
      if g.email:
         if request.method == 'POST' :
            sum = 0
            ll = []
            d = {}
            f = request.form
            for key in sorted(f.keys()):
                for value in f.getlist(key):
                    sum = sum + int(value)
                    ll.append(value)
                ll.append(sum)
                d[key] = ll 
                ll = []
                sum = 0 
            d['coursecode'] = coursecode
            d['internal'] = g.email
            s = test.insert_at_mid(d)
            return redirect('/t_index')
         else :
            mydata = {'session':'2018'}
            l=test.get_student(mydata)
            return render_template('t_at_mid.html',l=l,coursecode=coursecode)
            

      
		

		

if __name__ == '__main__':
   app.run(debug = True,host='0.0.0.0')
