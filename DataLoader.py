from models.user import User
from models.mountain import Mountain
from flask_bcrypt import generate_password_hash
import csv

class Loader():

    def __init__(self, db):
        self.__db = db



    def create_admin_user(self):
        admin = User()
        admin.username = "admin"
        admin.password = generate_password_hash("5uasdf3q7bzl77")
        admin.is_admin = True
        self.__db.create_user(admin)

    def create_mountains(self):
        with open("data/Gipfel.csv", "rt", encoding="iso-8859-1") as file:
            csv_reader = csv.reader(file, delimiter=';', quotechar='|')

            for row in csv_reader:
                name = row[0]
                height = row[1]
                kantons = row[4].split("/")
                x_cord = row[7]
                y_cord  = row[8]

                if name and height and kantons and x_cord and y_cord:
                    if name == "LK-Punkt" or name =="Name":
                        pass
                    else:
                        for kanton in kantons:
                            try:
                                self.__db.create_mountain(Mountain(
                                    name = name,
                                    kanton = kanton,
                                    hoehe = int(height),
                                    x_koordinate = int(x_cord),
                                    y_koordinate = int(y_cord)
                                ))
                            except:
                                print("{},{},{},{},{}".format(name, height, kantons[0], x_cord, y_cord))
                else:
                    print("{},{},{},{},{}".format(name, height, kantons[0], x_cord, y_cord))


    def load(self):
        self.create_admin_user()
        self.create_mountains()
