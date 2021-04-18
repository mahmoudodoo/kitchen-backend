from flask import jsonify, request, abort,make_response
from app import db
from app import app
from app.models.cook_model import Cook
import uuid





@app.route('/cooks', methods=['GET'])
def get_all_cooks():
    cooks= Cook.query.all()
    output = []
    if not cooks:
        return jsonify({'message':'No cooks!'})

    for cook in cooks:
        cook_data = {}
        cook_data['public_id'] =cook.public_id
        cook_data['name']= cook.cook_name
        cook_data['video_id'] = cook.video_id
        cook_data['steps'] = cook.steps
        cook_data['kitchen_id'] = cook.kitchen_id
        cook_data['image_url'] = '/static/image/cook/{}'.format(cook.public_id)
        output.append(cook_data)

    return jsonify({'cooks':output})

@app.route('/cooks/<public_id>',methods=['GET'])
def get_one_cook(public_id):
    cook = Cook.query.filter_by(public_id=public_id).first()
    if not cook:
        return jsonify({'message':'Cook not Found!!!!'})
    cook_data = {}
    cook_data['public_id'] =cook.public_id
    cook_data['name']= cook.cook_name
    cook_data['video_id'] = cook.video_id
    cook_data['steps'] = cook.steps
    cook_data['kitchen_id'] = cook.kitchen_id
    return jsonify({'cook':cook_data})

@app.route('/cooks',methods=['POST'])
def create_cook():
    data = request.get_json()
    new_kitchen = Cook(public_id=str(uuid.uuid4()), cook_name=data['name'],video_id=data['video_id'],steps=data['steps'],kitchen_id=data['kitchen_id'])
    db.session.add(new_kitchen)
    db.session.commit()
    return jsonify({'message' :'New cook has been created!'})


@app.route('/cooks/<public_id>',methods=['DELETE'])
def delete_cook(public_id):
    cook = Cook.query.filter_by(public_id=public_id).first()
    if not cook:
        return jsonify({'message':'Cook not Found!!!!'}),404
    db.session.delete(cook)
    db.session.commit()
    return jsonify({'message': 'Cook has been deleted!'}),200