from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from models import Base


class Mountain(UserMixin, Base):
    __tablename__ = "mountains"

    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    youtube_link = Column(String(100))
    gpx_file = Column(String(100))
    kanton = Column(String(50))
    hoehe = Column(Integer)
    x_koordinate = Column(Integer)
    y_koordinate = Column(Integer)
    rating = Column(Integer)
    difficulty = Column(Integer)
