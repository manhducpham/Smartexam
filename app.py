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

@app.route('/teacher')
def teacher():
    return render_template('teacher.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/teacher/qbank')
def qbank():
    return render_template('qbank.html')

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
# @app.route('/posts/<post_id>')
# def one_dict(post_id):
#     # all_post = Post.objects()
#     # for post in all_post:
#     #     if post[id] = post_id:
#     #         p = post
#     p = Post.objects().with_id(post_id)
#     return render_template('dict.html', post = p)

# @app.route('/posts')
# def multi_dict():
#     all_post = Post.objects()
#     return render_template('posts.html', posts = all_post)

# @app.route('/new-post', methods = ['GET', 'POST'])
# def new_post():
#     if request.method == 'GET':
#         return render_template('new_post.html')
#     elif request.method == 'POST':
#         # 1. Get form & extract data
#         form = request.form
#         t = form['title']
#         a= form['author']
#         c = form['content']
#         #Cách khi có database
#         new_post = Post(title = t, author = a, content = c, likes = 0)
#         new_post.save()
#         # Cách đầu tiên khi chưa có database
#         # new_p = {
#         #     'title': t,
#         #     'author': a,
#         #     'content': c,
#         # }
#         # # print(title, author, content)
#         # # 2. Add new post
#         # ps.append(new_p)
#         # return redirect('/posts')
#         return redirect(url_for('multi_dict'))
# @app.route('/delete/<post_id>')
# def del_post(post_id):
#     post = Post.objects().with_id(post_id)
#     post.delete()
#     return redirect('/posts')

# @app.route('/update/<post_id>', methods = ['GET', 'POST'])
# def update_post(post_id):
#     post = Post.objects().with_id(post_id)
#     if request.method == 'GET':
#         return render_template('update.html', post = post)
#     if request.method == 'POST':
#         form = request.form
#         t = form['title']
#         a= form['author']
#         c = form['content']
#         post.update(set__title = t, set__author = a, set__content = c)
#         return redirect('/posts')

if __name__ == "__main__":
    app.run(debug = True)