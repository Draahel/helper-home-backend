from config.db import  db, ma, app

class Aplication(db.Model):
    __tablename__ = "aplications"

    id = db.Column(db.Integer, primary_key =True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    publication = db.Column(db.Integer, db.ForeignKey('publications.id'), nullable=False)
    date = db.Column(db.Date())
    state = db.Column(db.Integer)
    last_stage = db.Column(db.String(100))
    cancel_date = db.Column(db.Date())

    def __init__(self, user, publication, date, state, last_stage, cancel_date):
        self.user = user
        self.publication = publication
        self.date = date
        self.state = state
        self.last_stage = last_stage
        self.cancel_date = cancel_date

with app.app_context():
    db.create_all()

class AplicationSchema(ma.Schema):
    class Meta:
        fields = ('id', "user", "publication", "date", "state", "last_stage", "cancel_date")
