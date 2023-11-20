from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.stage import Stage, StageSchema
from utils.general_response import success, error
from datetime import date as DateTime

route_stages = Blueprint("route_stages", __name__)

stage_schema = StageSchema()
stages_schema = StageSchema(many=True)

@route_stages.route('/stages', methods=['GET'])
def stage():
    aplication_id = request.args.get('aplication_id')
    if aplication_id:
        resultall = Stage.query.filter_by(aplication=aplication_id).all()
    else:
        resultall = Stage.query.all()
    result_stage = stages_schema.dump(resultall)
    return success(result_stage, True, 200)

@route_stages.route('/savestage', methods=['POST'])
def save():
    aplication = request.json['aplication']
    is_current = True
    date = DateTime.today()

    new_stage = Stage(aplication, is_current, date)
    db.session.add(new_stage)
    db.session.commit()
    return success(stage_schema.dump(new_stage), True, 202)


@route_stages.route('/updatestage', methods=['PUT'])
def Update():
    id = request.json['id']
    is_current = request.json['is_current']
    stage_update = Stage.query.get(id)
    if stage_update:
        stage_update.is_current = is_current
        db.session.commit()
        return success(stage_schema.dump(stage_update), True, 200)
    else:
        return error("Stage Not Found", 404)

@route_stages.route('/deletestage/<id>', methods=['DELETE'])
def delete(id):
    stage = Stage.query.get(id)
    db.session.delete(stage)
    db.session.commit()
    return success(stage_schema.dump(stage), True, 200)