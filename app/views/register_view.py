

from flask.helpers import url_for
from app import app
from flask import render_template
from flask import render_template, flash, redirect
from app.models.admin_model import Admin
from app import db
from app.forms.register_form import RegistrationForm
import requests

@app.route('/register',methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        payload = {'name':form.username.data,'password':form.password.data}
        r = requests.post('http://127.0.0.1:5000/users',json=payload) 
        if r.ok:
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))
        else:
            flash('Error: {}'.format(r.status_code))
    return render_template('register_template.html',title='Register', form=form)