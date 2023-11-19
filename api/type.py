from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.type import Type, TypeSchema

route_types = Blueprint("route_types", __name__)

type_schema = TypeSchema()
types_schema = TypeSchema(many=True)

@route_types.route('/types', methods=['GET'])
def type():
    resultall = Type.query.all()
    result_type = types_schema.dump(resultall)
    return jsonify(result_type)

@route_types.route('/savetype', methods=['POST'])
def save():
    type = request.json['type']
    new_type = Type(type)
    db.session.add(new_type)
    db.session.commit()
    return jsonify(type_schema.dump(new_type))


@route_types.route('/updatetype', methods=['PUT'])
def Update():
    id = request.json['id']
    type = request.json['type']
    type_update = Type.query.get(id)
    if type_update:
        print(type_update)
        type_update.type = type
        db.session.commit()
        return jsonify(type_schema.dump(type_update))
    else:
        return "Error"

@route_types.route('/deletetype/<id>', methods=['DELETE'])
def delete(id):
    type = Type.query.get(id)
    db.session.delete(type)
    db.session.commit()
    return jsonify(type_schema.dump(type))