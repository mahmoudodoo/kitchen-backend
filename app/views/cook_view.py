
from app import db
from app import app
from flask import render_template,flash, redirect,url_for,Flask
from app.forms.cook_form import AddCookForm,DeleteCookForm
from flask_login import login_required
from app import Config
import requests
from app.models.cook_model import Cook
from werkzeug.utils import secure_filename
import os

@app.route('/cook', methods=['GET', 'POST'])
@login_required
def cook():
    add_form = AddCookForm()
    if add_form.validate_on_submit():
        cook_name = add_form.cook_name.data
        cook_kitchen = add_form.kitchen.data
        video_id= add_form.video_id.data
        steps= add_form.steps.data
        cook_image = add_form.image.data
        print(cook_image)
        filename = secure_filename(cook_image.filename)
        cook_image.save(os.path.join(
            Config.STATIC_PATH, 'image/cook', filename
        ))
        data = {
            'name':cook_name,
            'video_id':video_id,
            'steps':steps,
            'kitchen_id':cook_kitchen.public_id
                }
        r= requests.post('http://127.0.0.1:5000/cooks',json=data)
        if r.ok:
            print('Cook has been added!!')
            cook = Cook.query.filter_by(cook_name=cook_name).first()
            old_image_path = os.path.join(Config.STATIC_PATH,'image/cook',filename)
            f, extension = os.path.splitext(old_image_path)
            new_image_path = os.path.join(Config.STATIC_PATH,'image/cook','{0}{1}'.format(cook.public_id,extension))
            os.rename(old_image_path,new_image_path)
            return redirect('home')


    delete_form = DeleteCookForm()
    if delete_form.validate_on_submit():
        cook_id = delete_form.cook_id.data
        r= requests.delete('http://127.0.0.1:5000/cooks/{}'.format(cook_id))
        if r.ok:
            image_path = os.path.join(Config.STATIC_PATH,'image/cook','{}.png'.format(cook_id))
            os.remove(image_path)
            print('This cook {} has been deleted!!'.format(cook_id))
            return redirect('home')
        if r.status_code == 404:
            flash('Cook ID not found!')
            return redirect(url_for('cook'))

    return render_template('cook_template.html',add_form =add_form,delete_form=delete_form)

