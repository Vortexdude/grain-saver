from app.database.db import db
from uuid import uuid4


class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.String(300), unique=True)
    event_name = db.Column(db.String(300))
    event_type = db.Column(db.String(300))
    event_location = db.Column(db.String(300))
    event_date = db.Column(db.String(300))
    event_time = db.Column(db.String(300))
    event_orgnizer = db.Column(db.String(300))
    event_orgnizer_id = db.Column(db.String(300))

    def __init__(
            self,
            event_name: str,
            event_type: str,
            event_location: str,
            event_date: str,
            event_time: str,
            event_orgnizer: str,
            event_orgnizer_id: str,
    ):
        self.event_id = str(uuid4())
        self.event_name = event_name
        self.event_type = event_type
        self.event_location = event_location
        self.event_date = event_date
        self.event_time = event_time
        self.event_orgnizer = event_orgnizer
        self.event_orgnizer_id = event_orgnizer_id

    @classmethod
    def find_byt_filter(cls, event_name, event_orgnizer):
        if event_name:
            return cls.query.filter_by(event_name=event_name).first()
        elif event_orgnizer:
            return cls.query.filter_by(event_name=event_name).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
