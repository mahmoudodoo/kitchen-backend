from app import db



class Kitchen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id= db.Column(db.String(50), unique=True)
    kitchen_name = db.Column(db.String(100))
    cooks = db.relationship("Cook", backref='kitchen', lazy='dynamic')
    