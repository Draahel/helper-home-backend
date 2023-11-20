from flask import Blueprint, request, jsonify
from config.db import db, app, ma
from models.publication import Publication, PublicationSchema
from models.user import User, UserSchema
from utils.general_response import success, error

route_publications = Blueprint("route_publications", __name__)

publication_schema = PublicationSchema()
publications_schema = PublicationSchema(many=True)

user_schema = UserSchema()

@route_publications.route('/publications', methods=['GET'])
def publication():
    user_id = request.args.get('user_id')
    publication_id = request.args.get('publication_id')
    if publication_id:
        #informacion detallada de publication y publicador
        result = db.session.query(Publication, User).\
            select_from(Publication).join(User).filter(Publication.id==publication_id).first()
        publication = publication_schema.dump(result[0])
        user = user_schema.dump(result[1])
        publication['user_info'] = user
        return success(publication, True, 200) 
    if user_id is not None:
        # Mis Publicaciones
        result = Publication.query.filter_by(user=user_id).all()
        publications = publications_schema.dump(result)
        return success(publications, True, 200)
    resultall = Publication.query.all()
    result_publication = publications_schema.dump(resultall)
    return success(result_publication, True, 200)

@route_publications.route('/savepublication', methods=['POST'])
def save():
    user = request.json['user']
    category = request.json['category']
    working_date = request.json['working_date']
    description = request.json['description']
    state = request.json['state']
    salary = request.json['salary']
    ubication = request.json['ubication']
    
    new_publication = Publication(user, category, working_date, description, state, salary, ubication)
    db.session.add(new_publication)
    db.session.commit()
    publication = publication_schema.dump(new_publication)
    return success(publication, True, 200)


@route_publications.route('/updatepublication', methods=['PUT'])
def Update():
    id = request.json['id']
    category = request.json['category']
    working_date = request.json['working_date']
    description = request.json['description']
    state = request.json['state']
    salary = request.json['salary']
    ubication = request.json['ubication']

    publication_update = Publication.query.get(id)
    if publication_update:
        publication_update.category = category
        publication_update.working_date = working_date
        publication_update.description = description
        publication_update.state = state
        publication_update.salary = salary
        publication_update.ubication = ubication
        db.session.commit()
        publication = publication_schema.dump(publication_update)
        return success(publication, True, 200)
    else:
        return error("Couldn't find publication", 402)

@route_publications.route('/deletepublication/<id>', methods=['DELETE'])
def delete(id):
    publication = Publication.query.get(id)
    if not publication:
        error("Couldn't find publication", 404)
    db.session.delete(publication)
    db.session.commit()
    result = publication_schema.dump(publication)
    return success(result, True, 200)