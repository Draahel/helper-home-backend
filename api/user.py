from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.user import User, UserSchema
from models.account import Account, AccountSchema

route_users = Blueprint("route_users", __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@route_users.route('/users', methods=['GET'])
def user():
    user_id = request.args.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        if not user:
            return "Error"
        else:
            return jsonify(user_schema.dump(user))
    else:
        resultall = User.query.all()
        result_user = users_schema.dump(resultall)
        return jsonify(result_user)

# @route_users.route('/saveuser', methods=['POST'])
# def save():
#     type = request.json['type']
#     document_type = request.json['document_type']
#     document_number = request.json['document_number']
#     nacionality = request.json['nacionality']
#     name = request.json['name'] 
#     lastname = request.json['lastname']
#     birthday = request.json['birthday']
#     gender = request.json['gender']
#     email = request.json['email']
#     address = request.json['address']
#     telephone = request.json['telephone']

#     query = select(User).where((User.email == email)|(User.document_number == document_number))
#     result = db.session.execute(query)
#     user = result.fetchone()

#     if user is not None:
#         return 'Already Exist'
#     else:
#         new_user = User(type, document_type, document_number, nacionality, name, lastname, birthday, gender, email, address, telephone)
#         db.session.add(new_user)
#         db.session.commit()
#         return jsonify(user_schema.dump(new_user))



@route_users.route('/updateuser', methods=['PUT'])
def Update():
    id = request.json['id']
    nacionality = request.json['nacionality']
    name = request.json['name']
    lastname = request.json['lastname']
    birthday = request.json['birthday']
    gender = request.json['gender']
    email = request.json['email']
    address = request.json['address']
    telephone = request.json['telephone']

    user = User.query.get(id)
    if user:
        if not user_schema.dump(user)['email'] == email:
            user_exist = Account.query.filter_by(email=email).first()
            if user_exist:
                return jsonify({"error":"Invalid Email", "success":False})
            
        account = Account.query.filter_by(email=user_schema.dump(user)['email']).first()
        account.email = email

        user.nacionality = nacionality
        user.name = name
        user.lastname = lastname
        user.birthday = birthday
        user.gender = gender
        user.email = email
        user.address = address
        user.telephone = telephone
        db.session.commit()


        return jsonify(user_schema.dump(user))
    else:
        return "Error"

@route_users.route('/deleteuser/<id>', methods=['DELETE'])
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user_schema.dump(user))