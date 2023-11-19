from config.db import  db, ma, app

class Type(db.Model):
    __tablename__ = "types"

    id = db.Column(db.Integer, primary_key =True)
    type = db.Column(db.String(50))

    def __init__(self, type):
        self.type = type

with app.app_context():
    db.create_all()

class TypeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'type')
