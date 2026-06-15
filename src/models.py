from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import Enum as pyEnum

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped [str] = mapped_column (String (20), nullable = False)
    surname: Mapped [str] = mapped_column (String (20), nullable = False)
    username: Mapped [str] = mapped_column (String (10), unique = True, nullable = False)
    email: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String (20), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planet (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped [str] = mapped_column (String (20), nullable = False)

class Gender (pyEnum):
    Female = 1
    Male = 2

class Specie (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped [str] = mapped_column (String (20), nullable = False)
    language: Mapped [str] = mapped_column (String(20))

class Character (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped [str] = mapped_column (String (20), nullable = False)
    description: Mapped [str] = mapped_column (String ())

    planet_id: Mapped [int]= mapped_column (ForeignKey ("planet.id"))
    planet: Mapped [Planet] = relationship ()

    specie_id: Mapped [int]= mapped_column (ForeignKey ("specie.id"))
    specie: Mapped [Specie] = relationship ()

    gender: Mapped [Gender] = mapped_column (Enum (Gender))

class Vehicle (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped [str] = mapped_column (String (20), nullable = False)
    description: Mapped [str] = mapped_column (String ())

class Favorite (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped [int]= mapped_column (ForeignKey ("User.id"))
    user: Mapped [User] = relationship ()

    character_id: Mapped [int] = mapped_column (ForeignKey ("Character.id"))
    character: Mapped [Character] = relationship ()

    planet_id: Mapped [int] = mapped_column (ForeignKey ("planet.id"))
    planet: Mapped [Planet] = relationship ()

    vehicle_id: Mapped [int] = mapped_column (ForeignKey ("vehicle.id"))
    vehicle: Mapped [Vehicle] = relationship ()

