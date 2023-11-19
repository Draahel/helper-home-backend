from config.db import  db, ma, app

class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key =True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, user, email, password):
        self.user = user
        self.email = email
        self.password = password

with app.app_context():
    db.create_all()

class AccountSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user', 'email', 'password')
