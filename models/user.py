from config.db import  db, ma, app

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key =True)
    type = db.Column(db.Integer, db.ForeignKey('types.id'))
    document_type = db.Column(db.Integer)
    document_number = db.Column(db.Integer)
    nacionality = db.Column(db.String(50))
    name = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    birthday = db.Column(db.Date())
    gender = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(50))
    telephone = db.Column(db.String(50))

    def __init__(self, type, document_type, document_number, nacionality, name, lastname, birthday, gender, email, address, telephone):
        self.type = type
        self.document_type = document_type
        self.document_number = document_number
        self.nacionality = nacionality
        self.name = name
        self.lastname = lastname
        self.birthday = birthday
        self.gender = gender
        self.email = email
        self.address = address
        self.telephone = telephone

with app.app_context():
    db.create_all()

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 
                  'type', 
                  'document_type', 
                  'document_number', 
                  'nacionality', 
                  'name', 
                  'lastname', 
                  'birthday', 
                  'gender', 
                  'email', 
                  'address', 
                  'telephone'
                )
