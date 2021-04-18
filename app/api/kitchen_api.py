from flask import jsonify, request, abort,make_response
from app import db
from app import app
from app.models.kitchen_model import Kitchen
import uuid





@app.route('/kitchens', methods=['GET'])
def get_all_kitchens():
    kitchens= Kitchen.query.all()
    output = []
    if not kitchens:
        return jsonify({'message':'No kitchens!'}),404

    for kitchen in kitchens:
        kitchen_data = {}
        kitchen_data['public_id'] =kitchen.public_id
        kitchen_data['name']= kitchen.kitchen_name
        kitchen_data['image_url'] = '/static/image/kitchen/{}'.format(kitchen.public_id)
        output.append(kitchen_data)

    return jsonify({'kitchens':output})

@app.route('/kitchens/<public_id>',methods=['GET'])
def get_one_kitchen(public_id):
    kitchen = Kitchen.query.filter_by(public_id=public_id).first()
    if not kitchen:
        return jsonify({'message':'Kitchen not Found!!!!'}),404
    kitchen_data = {}
    kitchen_data['public_id'] =kitchen.public_id
    kitchen_data['name']= kitchen.kitchen_name
    return jsonify({'kitchen':kitchen_data})

@app.route('/kitchens',methods=['POST'])
def create_kitchen():
    data = request.get_json()
    new_kitchen = Kitchen(public_id=str(uuid.uuid4()), kitchen_name=data['name'])
    db.session.add(new_kitchen)
    db.session.commit()
    return jsonify({'message' :'New kitchen has been created!'})


@app.route('/kitchens/<public_id>',methods=['DELETE'])
def delete_kitchen(public_id):
    kitchen = Kitchen.query.filter_by(public_id=public_id).first()
    if not kitchen:
        return jsonify({'message':'Kitchen not Found!!!!'}),404
    db.session.delete(kitchen)
    db.session.commit()
    return jsonify({'message': 'Kitchen has been deleted!'}),200