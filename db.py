import mysql.connector
from sqlalchemy import *
from sqlalchemy_utils import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models.user import User
from models.mountain import Mountain

class DB:

    def __init__(self):
        print("DB object created")
        self.__HOST = "127.0.0.1"
        self.__PORT = 3306
        self.__DATABASE = "peakview"
        self.Base = declarative_base()


    def create(self):
        try:
            
            create_database('mysql+mysqlconnector://{}:{}@{}:{}/{}'.format("root","", self.__HOST, self.__PORT, self.__DATABASE))
            print("Database created.")
        except mysql.connector.Error as err:
            print(err)
            print("Database already exists.")

    def create_tables(self):
        import models as db
        db.metadata.create_all(create_engine('mysql+mysqlconnector://{}:{}@{}:{}/{}'.format("root","", self.__HOST, self.__PORT, self.__DATABASE), echo=True))


    def delete(self):
        try:
            drop_database('mysql+mysqlconnector://{}:{}@{}:{}/{}'.format("root", "", self.__HOST, self.__PORT, self.__DATABASE))
            print("Database deleted successfully.")
        except:
            print("Database does not exist.")

    def connect(self):
        try:
            self.__engine = create_engine('mysql+mysqlconnector://{}:{}@{}:{}/{}'.format("root","", self.__HOST, self.__PORT, self.__DATABASE), echo=True)
            self.__Session = sessionmaker(bind=self.__engine)
            self.session = self.__Session()
            self.Base.metadata.bind = self.__engine
            print("Connected with {} on {}".format(self.__DATABASE, self.__HOST))
        except mysql.connector.Error as err:
            print(err)

    def create_user(self, user):
        self.session.add(user)
        self.session.commit()


    def read_user(self, username):
        return self.session.query(User).filter_by(username = username).first()


    def create_mountain(self, mountain):
        self.session.add(mountain)
        self.session.commit()
        print("Mountain created")

    def read_mountain_by_name(self, name):
        return self.session.query(Mountain).filter_by(name = name).first()

    def read_mountain_by_id(self, mountain_id):
        return self.session.query(Mountain).filter_by(id = mountain_id).first()

    def read_user_by_id(self, user_id):
        return self.session.query(User).filter_by(id = user_id).first()

    def read_mountains_by_kanton(self, kanton):
        return self.session.query(Mountain).filter_by(kanton = kanton).all()

    def read_mountains(self):
        return self.session.query(Mountain).all()

    def update_mountain(self, mountain):
        self.session.add(mountain)
        self.session.commit()

    def delete_mountain(self, mountain):
        self.session.delete(mountain)
        self.session.commit()
