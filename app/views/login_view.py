
from flask.helpers import url_for
from app import app
from flask import render_template,flash, redirect
from app.forms.login_form import LoginForm
from app.models.admin_model import Admin
import requests
from flask_login import logout_user,login_user,current_user




# Create login form view
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(name=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template('login_template.html', title='Sign In', form=form)



# Create Log out function
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# Create login form view
# @app.route('/', methods=['GET', 'POST'])
# @app.route('/login', methods=['GET', 'POST'])
# def login():

#     form = LoginForm()
#     user = form.username.data
#     password = form.password.data
#     if form.validate_on_submit():
#         r = requests.get('http://127.0.0.1:5000/login_api',auth=requests.auth.HTTPBasicAuth(user, password))
#         if r.ok:
#             print(r.text)
#             return redirect(url_for('home'))
#         else:
#             flash('Invalid username or password {}'.format(r.status_code))

#     return render_template('login_template.html', title='Sign In', form=form)



# def is_auth(self,username,password):
#     r = requests.get('http://127.0.0.1:5000/login_api',auth=requests.auth.HTTPBasicAuth(user, password))
#     print(r.text)

# Create Log out function
# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('login'))
