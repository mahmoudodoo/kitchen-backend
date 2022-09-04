
from app import db
from app import app
from flask import render_template,flash, redirect,request
from flask_login import login_required
import requests
import os
from app import Config

host_name = "localhost:5000"
@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'GET':
        r = requests.get(f'http://{host_name}/kitchens')
        try:
            kitchens = r.json()['kitchens']
        except KeyError:
            kitchens = {}

    return render_template('home_template.html',kitchens=kitchens)
