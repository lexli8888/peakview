import sqlalchemy.ext.declarative as sad

Base = sad.declarative_base()
metadata = Base.metadata

from models.user import *
from models.mountain import *