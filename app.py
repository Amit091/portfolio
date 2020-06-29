from flask import Flask, render_template, request, redirect, url_for
import time
import csv
app = Flask(__name__)
  
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        dat={'time':time.time(), 'email':email,'subject':subject,'message':message}
        file = db.write(f'\n{dat}')

def write_to_csv(data):
    with open('database.csv', mode='a',newline='') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        dat = {'time': time.time(), 'email': email, 'subject': subject, 'message': message}
        fields = ['time', 'email','subject','message']
        writer = csv.DictWriter(db2, fieldnames=fields)
        writer.writeheader()
        writer.writerow(dat)
@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:            
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thanks.html')
        except:
            return 'did not save to database'
    else:
        return render_template('contact.html')



