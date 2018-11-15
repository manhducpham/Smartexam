from flask import Flask, render_template, request, redirect, url_for
import mlab_user
# import mlab_verifyuser
import verify_email
from verifyuser import Verifyuser
from user import User

app = Flask(__name__)
mlab_user.connect()
# mlab_verifyuser.connect()

@app.route('/welcome/<user_id>')
def welcome(user_id):
    user = User.objects().with_id(user_id)
    return render_template('home.html', user = user)
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', error = "")
    elif request.method == 'POST':
        form = request.form
        user_id = form['user_id']
        password = form['password']
        all_users = User.objects()
        error = None
        for u in all_users:
            if u["user_id"] == user_id and u['password'] == password:
                return redirect(url_for('welcome', user_id = u['id']))
            else:
                error = 'Invalid Credentials. Please try again.'
        return render_template('login.html', error = error)

@app.route('/verifyuser/<verifyuser_id>', methods = ['GET', 'POST'])
def verifyuser(verifyuser_id):
    verify_user = Verifyuser.objects().with_id(verifyuser_id)
    if request.method == 'GET':
        return render_template('verify_user.html', verify_user = verify_user)
    elif request.method == 'POST':
        form = request.form
        code = form['code']
        if code == verify_user['code']:
            user_id = verify_user['user_id']
            full_name = verify_user['full_name']
            email = verify_user['email']
            password = verify_user['password']
            new_user = User(user_id = user_id, full_name = full_name, email = email, password = password)
            new_user.save()
            verify_user.delete()
            return redirect(url_for('login'))
        else:
            return redirect(url_for('verify_user',verifyuser_id = new_user['id']))

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html', error = "")
    elif request.method == 'POST':
        form = request.form
        user_id = form['user_id']
        full_name = form['full_name']
        email = form['email']
        password = form['password']
        code = verify_email.verify_code()
        all_users = User.objects()
        user_id_list = []
        for u in all_users:
            user_id_list.append(u['user_id'])
        if user_id in user_id_list:
            error = "User ID is already existed, please choose another User ID"
            return render_template('signup.html', error = error)
        else:
            new_verify_user = Verifyuser(user_id = user_id, full_name = full_name, email = email, password = password, code = code)
            new_verify_user.save()        
            verify_email.verify_email(email, full_name, code)
            return redirect(url_for('verifyuser', verifyuser_id = new_verify_user['id']))

@app.route('/teacher/qbank', methods = ['GET', 'POST'])
def qbank():
    if request.method == 'GET':
        return render_template('qbank.html')
    elif request.method == 'POST':
        form = request.form

@app.route('/teacher/scores_export')
def scores_export():
    return render_template('scores_export.html')

@app.route('/teacher/exam_print')
def exam_print():
    return render_template('exam_print.html')

@app.route('/student/score')
def score():
    return render_template('score.html')

@app.route('/student/practice')
def practice():
    return render_template('practice.html')

@app.route('/student/exam')
def exam():
    return render_template('exam.html')

@app.route('/')
def homepage():
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug = True)