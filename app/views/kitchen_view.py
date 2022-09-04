
from app import db
from app import app
from app import Config
from flask import render_template,flash, redirect,request,send_from_directory,url_for,Flask
from app.forms.kitchen_form import AddKitchenForm,DeleteKitchenForm
from flask_login import login_required
from werkzeug.utils import secure_filename
import os
import requests
from app.models.kitchen_model import Kitchen
from app.models.cook_model import Cook
import json


host_name = "localhost:5000"
@app.route('/kitchen', methods=['GET', 'POST'])
@login_required
def kitchen():
    add_form = AddKitchenForm()
    if add_form.validate_on_submit():
        kitchen_name = add_form.kitchen_name.data
        kitchen_image = add_form.image.data
        print(kitchen_image)
        filename = secure_filename(kitchen_image.filename)
        kitchen_image.save(os.path.join(
            Config.STATIC_PATH, 'image/kitchen', filename
        ))
        data = {'name':kitchen_name}
        r= requests.post(f'http://{host_name}/kitchens',json=data)
        if r.ok:
            print('Kitchen has been added!!')
            kitchen = Kitchen.query.filter_by(kitchen_name=kitchen_name).first()
            old_image_path = os.path.join(Config.STATIC_PATH,'image/kitchen',filename)
            f, extension = os.path.splitext(old_image_path)
            new_image_path = os.path.join(Config.STATIC_PATH,'image/kitchen','{0}{1}'.format(kitchen.public_id,extension))
            os.rename(old_image_path,new_image_path)
            return redirect('home')

    delete_form = DeleteKitchenForm()
    if delete_form.validate_on_submit():
        kitchen_id = delete_form.kitchen_id.data
        r= requests.delete(f'http://{host_name}/kitchens/{kitchen_id}')
        if r.ok:
            image_path = os.path.join(Config.STATIC_PATH,'image/kitchen','{}.png'.format(kitchen_id))
            os.remove(image_path)
            print('This kitchen {} has been deleted!!'.format(kitchen_id))
            return redirect('home')
        if r.status_code == 404:
            flash('Kitchen ID not found!')
            return redirect(url_for('kitchen'))
    return render_template('kitchen_template.html',add_form =add_form,delete_form=delete_form)


@app.route('/kitchen/cooks/<public_id>', methods=['GET', 'POST'])
@login_required
def kitchen_cooks(public_id):
    if request.method == 'GET':
        r = requests.get(f'http://{host_name}/cooks')
        try:
            cooks = r.json()['cooks']
            output_dict = [x for x in cooks if x['kitchen_id'] == public_id]
        except KeyError:
            output_dict = {}

    return render_template('kitchen_cooks_template.html',cooks=output_dict)
