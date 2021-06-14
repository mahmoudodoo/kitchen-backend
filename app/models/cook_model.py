from app import db


class Cook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id= db.Column(db.String(50), unique=True)
    cook_name = db.Column(db.String(80))
    video_id = db.Column(db.String(300))
    steps = db.Column(db.String(300))
    kitchen_id = db.Column(db.String(50), db.ForeignKey('kitchen.public_id'))

    def __repr__(self):
        return '<Choice {}>'.format(self.name)