from app import db


class posts(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    post=db.Column(db.String(20))
    contact=db.Column(db.String(14))
    email=db.Column(db.String(60))

    def __repr__(self):
        return '<posts %r>' % (self.name)
