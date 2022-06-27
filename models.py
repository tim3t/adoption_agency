from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default='https://media.istockphoto.com/vectors/bird-cat-dog-vector-id476479065?k=20&m=476479065&s=612x612&w=0&h=hdOI2ncJa0E5xBBzCQsx8ip8haZo2gVAs6_lnETuhu8=')
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"<Pet {self.id} {self.name} {self.species}>"