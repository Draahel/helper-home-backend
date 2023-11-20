from config.db import  db, ma, app

class Publication(db.Model):
    __tablename__ = "publications"

    id = db.Column(db.Integer, primary_key =True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category = db.Column(db.String(100))
    working_date = db.Column(db.String(200))
    description = db.Column(db.String(200))
    state = db.Column(db.Integer)
    salary = db.Column(db.String(100))
    ubication = db.Column(db.String(200))

    def __init__(self, user, category, working_date, description, state, salary, ubication):
        self.user = user
        self.category = category
        self.working_date = working_date
        self.description = description
        self.state = state
        self.salary = salary
        self.ubication = ubication

with app.app_context():
    db.create_all()

class PublicationSchema(ma.Schema):
    class Meta:
        fields = ('id', "user", "category", "working_date", "description", "state", "salary", "ubication")
