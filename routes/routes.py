from flask import Flask, request, url_for, render_template, flash, redirect
from app import app

@app.route('/')
def index():
    return render_template(url_for('index.html'))



@app.route("/regiter", methods = ["GET", "POST"])
def register_user():
    from notebook_users import User
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        phone = request.form('number')
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if User.register_user_error_log == []
            User.user_registration(username,email,phone_number,password,confirm_password)
            flash("You have successfully registered!")
            return redirect(url_for('login.html'))
        else:
            flash(User.user_registration)
            return redirect(url_for('index.html'))

@app.route("/login", methods = ["GET", "POST"])
def login_user():
    from notebook_users import User
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if login_user_error_log == []:
            User.my_login(username,password)
            flash('logged in')
            return redirect(url_for('/view_memo.html'))
        else:
            flash(User.login_user_error_log)
            return redirect(url_for('index.html'))


if __name__ == '__main__':
    app.run(debug = True)
