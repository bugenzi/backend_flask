from app import db 

class Auth(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(120),nullable=False)

    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age

    # def __repr__(self):
    #     return f":{self.name}:{self.age}"

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_username(cls,username):
        return cls.query.filter_by(username = username).first()
        