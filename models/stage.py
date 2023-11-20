from config.db import  db, ma, app

class Stage(db.Model):
    __tablename__ = "stages"

    id = db.Column(db.Integer, primary_key =True)
    aplication = db.Column(db.Integer, db.ForeignKey("aplications.id"), nullable=False)
    is_current = db.Column(db.Boolean)
    date = db.Column(db.Date())

    def __init__(self, aplication, is_current, date):
        self.aplication = aplication
        self.is_current = is_current
        self.date = date

with app.app_context():
    db.create_all()

class StageSchema(ma.Schema):
    class Meta:
        fields = ('id', 'aplication', 'is_current', 'date')
