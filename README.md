# Star Wars Blog Database Model

> A SQLAlchemy-based database model for a Star Wars blog application, featuring user management, character and planet information, and favorite system. This project demonstrates database modeling and relationships using SQLAlchemy.

[![Flask](https://img.shields.io/badge/Flask-3.0.2-green.svg)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-blue.svg)](https://www.sqlalchemy.org/)
[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Keywords:** Flask, SQLAlchemy, Database Modeling, Star Wars, Python, Backend Development

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Database Models](#database-models)
- [Generating the Database Diagram](#generating-the-database-diagram)
- [Development](#development)
- [License](#license)
- [Contact](#contact)

## Features

- Complete Star Wars blog database model
- User management system
- Character information storage
- Planet information storage
- Favorite system for characters and planets
- Automatic diagram generation
- Clean and maintainable codebase

## Tech Stack

- **Backend:**
  - Flask 3.0.2
  - SQLAlchemy 2.0+
  - Python 3.13+

- **Development Tools:**
  - pipenv for package management
  - Graphviz for diagram generation
  - SQLite for database
  - Git for version control
  - VS Code (recommended IDE)

## Project Structure

```
/
├── src/
│   ├── models.py        # Database models and diagram generation
│   ├── main.py         # API endpoints
│   ├── utils.py        # Utility functions
│   └── admin.py        # Admin panel configuration
├── scripts/
│   ├── init_db.py      # Database initialization
│   └── generate_diagram.py # Diagram generation script
├── instance/
│   └── database.db     # SQLite database file
├── Pipfile            # Project dependencies
└── README.md         # Project documentation
```

## Setup & Installation

1. Enter the virtual environment:

   ```sh
   pipenv shell
   ```

2. Install dependencies:

   ```sh
   pipenv install
   ```

3. Initialize the database:
   ```sh
   python scripts/init_db.py
   ```

## Database Models

The project includes four main models that follow the format:

```
TableName
-
column_name data_type constraints
```

1. **User Model**

   ```python
   class User(db.Model):
       id: Mapped[int] = mapped_column(primary_key=True)
       email: Mapped[str] = mapped_column(String(120), unique=True)
       password: Mapped[str] = mapped_column(nullable=False)
       name: Mapped[str] = mapped_column(String(80))
       is_active: Mapped[bool] = mapped_column(Boolean())
       created_at: Mapped[datetime] = mapped_column(DateTime)
   ```

2. **Character Model**

   ```python
   class Character(db.Model):
       id: Mapped[int] = mapped_column(primary_key=True)
       name: Mapped[str] = mapped_column(String(100))
       gender: Mapped[str] = mapped_column(String(20))
       homeworld_id: Mapped[int] = mapped_column(ForeignKey("planet.id"))
       description: Mapped[str] = mapped_column(Text)
   ```

3. **Planet Model**

   ```python
   class Planet(db.Model):
       id: Mapped[int] = mapped_column(primary_key=True)
       name: Mapped[str] = mapped_column(String(100))
       climate: Mapped[str] = mapped_column(String(100))
       terrain: Mapped[str] = mapped_column(String(100))
       population: Mapped[str] = mapped_column(String(20))
   ```

4. **Favorite Model**
   ```python
   class Favorite(db.Model):
       id: Mapped[int] = mapped_column(primary_key=True)
       user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
       character_id: Mapped[int] = mapped_column(ForeignKey("character.id"))
       planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"))
       created_at: Mapped[datetime] = mapped_column(DateTime)
   ```

## Generating the Database Diagram

You can generate the database diagram in two ways:

1. Using the pipenv command:

   ```sh
   pipenv run diagram
   ```

2. Using Python directly:
   ```sh
   python src/models.py
   ```

Both commands will generate a `diagram.txt` file in the root directory with the complete database schema.

## Development

This project demonstrates:

- Database modeling with SQLAlchemy
- Entity relationships and foreign keys
- Database diagram generation
- Flask integration with SQLAlchemy
- Admin panel implementation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**Dante Fasano** - [GitHub](https://github.com/dantefasano)

Project Link: [https://github.com/dantefasano/starwars-db-model](https://github.com/dantefasano/starwars-db-model)

---

Made with ❤️ by Dante Fasano
