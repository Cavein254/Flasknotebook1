from flask import Flask, request, url_for, render_template, flash, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route("/regiter", methods = ["GET", "POST"])
def register_user():
    from models.notebook_users import User
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        phone_number = request.form['phone']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        role = request.form['role']

        
        new_user = User()
        new_user.user_registration(username = username,email = email,phone_number = phone_number,
                                    role = role,password =password,confirm_password =confirm_password)
        if User.register_user_error_log == []:
            flash("You have successfully registered!")
            return redirect('users')
        else:
            flash("User registration falled")
            errors = User.register_user_error_log
            return render_template('error.html', errors = errors)
    return render_template('regiter.html')

@app.route('/login', methods = ["GET", "POST"])
def login_user():
    from models.notebook_users import User
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        loggedin = User()
        loggedin.my_login(email = email,password = password)
        if loggedin.login_user_error_log == []:
            return render_template('user_action.html')
        else:
            flash(loggedin.login_user_error_log)
            return render_template('index.html')
    return render_template('login.html')

@app.route('/users', methods = ['GET', 'POST'])
def admin_list_users():
    from models.notebook_users import User
    user_admin = User()
    all_users = user_admin.admin_view_all_users()
    return render_template('users.html', users = all_users)

@app.route('/my_memos', methods = ['GET', 'POST'])
def user_memo():
    from models.notebook_memo import UserMemo
    if request.method == 'GET':
        get_memos = UserMemo()
        memos = get_memos.view_my_memos()
        return render_template('my_memos.html', memos = memos)
    return render_template('user_action.html')