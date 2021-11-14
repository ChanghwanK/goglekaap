from goglekaap import db


class User(db.Model):
    __tablename__ = 'USER'

    id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String(128), unique=True, nullable=False)
    password: str = db.Column(db.String(256), nullable=False)
    nick_name: str = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return "<User('%s', '%s')>" % (self.email, self.nick_name)