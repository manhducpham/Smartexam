from flask import Flask, render_template, request, redirect, url_for
import mlab_user
from user import User

app = Flask(__name__)
mlab_user.connect()

@app.route('/wronglogin', methods = ['GET', 'POST'])
def wronglogin():
    if request.method == 'GET':
        return render_template('wronglogin.html')
    elif request.method == 'POST':
        form = request.form
        user_id = form['user_id']
        password = form['password']
        all_users = User.objects()
        error = None
        for u in all_users:
            if u["user_id"] == user_id and u['password'] == password:
                print('OK')
                return render_template('logedin.html', user = u)
            else:
                print('Not ok')
                error = 'Invalid Credentials. Please try again.'
        return render_template('wronglogin.html', error = error)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form
        user_id = form['user_id']
        password = form['password']
        all_users = User.objects()
        error = None
        for u in all_users:
            if u["user_id"] == user_id and u['password'] == password:
                return render_template('logedin.html', user = u)
            else:
                error = 'Invalid Credentials. Please try again.'
        return render_template('wronglogin.html', error = error)


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        form = request.form
        user_id = form['user_id']
        email = form['email']
        password = form['password']
        new_user = User(user_id = user_id, email = email, password = password)
        new_user.save()
        return redirect(url_for('login'))

@app.route('/')
def homepage():
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug = True)