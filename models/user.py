from sqlalchemy import Column, Integer, String, Date, Boolean
from flask_login import UserMixin
from models import Base


class User(UserMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    username = Column(String(50))
    password = Column(String(100))
    is_activated = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    last_login = Column(Date)

