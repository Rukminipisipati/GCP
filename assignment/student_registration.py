import tempfile
import os
import io
from flask import flash,redirect
from flask import Flask,render_template,request,jsonify
from pyrebase import pyrebase
firebaseconfig = {
  "apiKey": "AIzaSyAYs2AJV1aL5XTPmbrO-M4PnP6K8a6KTt8",
  "authDomain": "registration-94334.firebaseapp.com",
  "databaseURL": "https://registration-94334-default-rtdb.firebaseio.com",
  "projectId": "registration-94334",
  "storageBucket": "registration-94334.appspot.com",
  "messagingSenderId": "326013991328",
  "appId": "1:326013991328:web:484ec6273884b1b7544cc5"
}
firebase = pyrebase.initialize_app(firebaseconfig)
db = firebase.database()

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

def hello_world():
    return render_template('login.html')
@app.route('/registration',methods=['GET','POST'])
def registration():
    print('registrations page')
    if request.method == 'POST':
        fname = request.form['firstname']
        lname = request.form['lastname']
        email = request.form['email']
        sid = request.form['sid']
        address = request.form['address']
        phn=request.form['phn']
        if len(fname)!=0 and len(lname)!=0 and len(email)!=0 and len(sid)!=0 and len(address)!=0 and len(phn):
            user_ref = db.child('Users').push({

                'sid':sid,
                'firstname': fname,
                'lastname': lname,
                'email' : email,
                'address':address,
                'phn' : phn
            })
        cr = db.child('Users').get()
        cr = dict(cr.val())
        for i in cr:
            if (sid == cr[i]['sid']):
                return render_template('./userdetails.html',result=cr[i])
    return render_template('login.html')

if __name__ == '__main__':

    app.run(debug=True)