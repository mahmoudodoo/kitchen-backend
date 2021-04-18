
from app import db
from app import app
from flask import render_template,flash, redirect,request
from flask_login import login_required
import requests
import os
from app import Config


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'GET':
        r = requests.get('http://127.0.0.1:5000/kitchens')
        try:
            kitchens = r.json()['kitchens']
        except KeyError:
            kitchens = {}

    return render_template('home_template.html',kitchens=kitchens)