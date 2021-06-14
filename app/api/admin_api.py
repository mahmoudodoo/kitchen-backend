from flask import jsonify, request, abort,make_response
from app import db
from app import app
from app.models.admin_model import Admin
import uuid
from werkzeug.security import generate_password_hash,check_password_hash
import jwt
import datetime
from functools import wraps


@app.route('/users', methods=['GET'])
def get_all_users():
    users= Admin.query.all()
    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] =user.public_id
        user_data['name']= user.name
        user_data['password']= user.password
        output.append(user_data)

    return jsonify({'users':output})

@app.route('/users/<public_id>',methods=['GET'])
def get_one_user(public_id):
    user = Admin.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message':'Admin not Found!!!!'})
    user_data = {}
    user_data['public_id'] =user.public_id
    user_data['name']= user.name
    user_data['password']= user.password
    return jsonify({'user':user_data})

@app.route('/users',methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'],method='sha256')
    new_user = Admin(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message' :'New Admin has been created!'})


@app.route('/users/<public_id>',methods=['DELETE'])
def delete_user(public_id):
    user = Admin.query.filter_by(public_id=public_id).first()
    userName = user.name
    userId = user.public_id
    if not user:
        return jsonify({'message':'Admin not Found!!!!'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({
            'message': 'This user {0} has been deleted!! ID: {1}'.format(str(userName),str(userId))
                })


@app.route('/login_api')
def login_api():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify ',401,{'WWW-Authenticate':'Basic realm="Login requierd!"'})

    user = Admin.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('Could not verify ',401,{'WWW-Authenticate':'Basic realm="Login requierd!"'})

    if check_password_hash(user.password,auth.password):
        token = jwt.encode({'public_id':user.public_id,'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)}, app.config['SECRET_KEY'])
        return jsonify({'token':token.decode('UTF-8'),'user_id':user.public_id,'username':user.name})

    return make_response('Could not verify ',401,{'WWW-Authenticate':'Basic realm="Login requierd!"'})
