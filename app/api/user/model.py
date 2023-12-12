from app.database.db import db
from uuid import uuid4

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(300), unique=True)
    fname = db.Column(db.String(300), unique=True)
    lname = db.Column(db.String(300), unique=False)
    location = db.Column(db.String(300), unique=True)
    phone = db.Column(db.String(300), nullable=True)
    password = db.Column(db.String(300), nullable=False)

    def __init__(self,
            fname,
            lname,
            location,
            phone,
            password
    ):
        """"
        We have created a constructor so that all the variables of the class
        object will be created when we call 
        
        user = User(var1, var2) 
        above line will create a class with thier properties like 

        user.var1
        user.var2
        likewise we will send the object to save_to_db method using self keyword
        so we can send via save_to_db method
        and they will be sent to the save_to_db method.
        """
        self.user_id = str(uuid4())
        self.fname = fname
        self.lname = lname
        self.location = location
        self.phone = phone
        self.password = password

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_filter(cls, phone = None, password = None, fname = None):
        if phone:
            return cls.query.filter_by(phone=phone).first()
        if password:
            return cls.query.filter_by(password=password).first()
        if fname:
            return cls.query.filter_by(fname=fname).first()

    @classmethod
    def login(cls, phone, password):
        user = cls.find_by_filter(phone=phone)
        if user:
            result = cls.find_by_filter(password=password)
            if result:
                return result
        else:
            return None

    @classmethod
    def to_json(cls):
        pass