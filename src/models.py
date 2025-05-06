from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy_schemadisplay import create_schema_graph
import enum

db = SQLAlchemy()

class FavoriteType(enum.Enum):
    CHARACTER = "character"
    PLANET = "planet"

class User(db.Model):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    # Relationships
    favorites = relationship("Favorite", back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "created_at": self.created_at.isoformat()
        }

class Character(db.Model):
    __tablename__ = 'characters'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    gender: Mapped[str] = mapped_column(String(20))
    homeworld_id: Mapped[int] = mapped_column(ForeignKey("planets.id"))
    description: Mapped[str] = mapped_column(Text)
    
    # Relationships
    homeworld = relationship("Planet", back_populates="residents")
    favorites = relationship("Favorite", back_populates="character")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "description": self.description
        }

class Planet(db.Model):
    __tablename__ = 'planets'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    climate: Mapped[str] = mapped_column(String(100))
    terrain: Mapped[str] = mapped_column(String(100))
    population: Mapped[str] = mapped_column(String(20))
    
    # Relationships
    residents = relationship("Character", back_populates="homeworld")
    favorites = relationship("Favorite", back_populates="planet")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population
        }

class Favorite(db.Model):
    __tablename__ = 'favorites'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    character_id: Mapped[int] = mapped_column(ForeignKey("characters.id"))
    planet_id: Mapped[int] = mapped_column(ForeignKey("planets.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "created_at": self.created_at.isoformat()
        }

def generate_diagram():
    # Get the absolute path for the output file
    diagram_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'diagram.txt')
    
    # Create the diagram content
    diagram_content = """# 1. Entities
# 2. Properties
# 3. Relationships

User
-
id integer PK
email string unique
password string
name string
is_active boolean
created_at datetime

Character
-
id integer PK
name string
gender string
homeworld_id integer FK >- Planet.id
description text

Planet
-
id integer PK
name string
climate string
terrain string
population string

Favorite
-
id integer PK
user_id integer FK >- User.id
character_id integer FK >- Character.id
planet_id integer FK >- Planet.id
created_at datetime
"""
    
    # Write the diagram to a file
    with open(diagram_path, 'w') as f:
        f.write(diagram_content)
    print(f"Diagram generated successfully at: {diagram_path}")

if __name__ == '__main__':
    generate_diagram()
