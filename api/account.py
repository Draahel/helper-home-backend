from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.account import Account, AccountSchema
from models.user import User, UserSchema
from sqlalchemy.future import select
from sqlalchemy import or_

route_accounts = Blueprint("route_accounts", __name__)

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)

user_schema = UserSchema()

@route_accounts.route('/account', methods=['GET'])
def account():
    email = request.args.get('email')
    password = request.args.get('pass')
    if email is None or password is None:
        return jsonify({'error': 'Insufficient parameters', "success":False}), 404

    result = Account.query.filter_by(email=email).first()
    if result is None:
        return jsonify({"error": "Invalid Data", "success":False})
    
    account = account_schema.dump(result)
    if not account['password'] == password:
       return jsonify({"error": "Invalid Data", "success":False})
    
    user = User.query.get(account['user'])
    if user is None:
        return jsonify({"error": "Any was wrong", "success":False}), 500
    
    return jsonify({"data": user_schema.dump(user), "success":True})
    

@route_accounts.route('/saveaccount', methods=['POST'])
def save():
    type = request.json['type']
    document_type = request.json['document_type']
    document_number = request.json['document_number']
    nacionality = request.json['nacionality']
    name = request.json['name']
    lastname = request.json['lastname']
    birthday = request.json['birthday']
    gender = request.json['gender']
    email = request.json['email']
    address = request.json['address']
    telephone = request.json['telephone']

    password = request.json['password']

    query = select(User).where(or_(User.email == email, User.document_number == document_number))
    result = db.session.execute(query)
    account = result.fetchone()

    if not account is None:
        return jsonify({"error": "User already Exist", "success":False})
    else:
        new_user = User(type, document_type, document_number, nacionality, name, lastname, birthday, gender, email, address, telephone)
        db.session.add(new_user)
        db.session.commit()
        user = user_schema.dump(new_user)
        
        new_account = Account(user['id'], email, password)
        db.session.add(new_account)
        db.session.commit()
        return jsonify({"data": user, "success":True})



@route_accounts.route('/updateaccount', methods=['PUT'])
def Update():
    id = request.json['id']
    password = request.json['password']

    account = Account.query.get(id)
    
    if account:
        account.password = password
        db.session.commit()
        return jsonify(account_schema.dump(account))
    else:
        return "Error"

@route_accounts.route('/deleteaccount/<id>', methods=['DELETE'])
def delete(id):
    account = Account.query.get(id)
    db.session.delete(account)
    db.session.commit()
    return jsonify(account_schema.dump(account))