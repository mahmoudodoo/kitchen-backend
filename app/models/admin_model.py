from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# from app.models.PaginatedAPIMixin import PaginatedAPIMixin
from app import login


@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))

class Admin(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    public_id= db.Column(db.String(50), unique=True)
    name = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<Users {}>'.format(self.name)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)