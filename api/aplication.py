from flask import Blueprint, request, jsonify
from config.db import db, app, ma
from models.aplication import Aplication, AplicationSchema
from utils.general_response import success, error
from sqlalchemy.sql import and_

route_aplications = Blueprint("route_aplications", __name__)

aplication_schema = AplicationSchema()
aplications_schema = AplicationSchema(many=True)

@route_aplications.route('/aplications', methods=['GET'])
def aplication():
    user_id = request.args.get('user_id')
    publication_id = request.args.get('publication_id')
    if user_id or publication_id:
        if user_id and publication_id:
            result = Aplication.query.filter(Aplication.user==user_id, Aplication.id==publication_id).all()
        elif user_id:
            result = Aplication.query.filter_by(user=user_id).all()
        elif publication_id:
            result = Aplication.query.filter_by(id=publication_id).all()
        aplications = aplications_schema.dump(result)
        return success(aplications, True, 200)
        
    resultall = Aplication.query.all()
    result_aplication = aplications_schema.dump(resultall)
    return success(result_aplication, True, 200)

@route_aplications.route('/saveaplication', methods=['POST'])
def save():
    user = request.json['user']
    publication = request.json['publication']
    date = request.json['date']
    state = request.json['state']
    last_stage = request.json['last_stage']
    cancel_date = None if not request.json['cancel_date'] else request.json['cancel_date']
    
    new_aplication = Aplication(user,  publication, date, state, last_stage, cancel_date)
    db.session.add(new_aplication)
    db.session.commit()
    aplication = aplication_schema.dump(new_aplication)
    return success(aplication, True, 200)


@route_aplications.route('/updateaplication', methods=['PUT'])
def Update():
    id = request.json['id']
    state = request.json['state']
    last_stage = request.json['last_stage']
    cancel_date = None if not request.json['cancel_date'] else request.json['cancel_date']

    aplication_update = Aplication.query.get(id)
    if aplication_update:
        aplication_update.state = state
        aplication_update.last_stage = last_stage
        aplication_update.cancel_date = cancel_date
        db.session.commit()
        aplication = aplication_schema.dump(aplication_update)
        return success(aplication, True, 200)
    else:
        return error("Couldn't find aplication", 402)

@route_aplications.route('/deleteaplication/<id>', methods=['DELETE'])
def delete(id):
    aplication = Aplication.query.get(id)
    if not aplication:
        error("Couldn't find aplication", 404)
    db.session.delete(aplication)
    db.session.commit()
    result = aplication_schema.dump(aplication)
    return success(result, True, 200)