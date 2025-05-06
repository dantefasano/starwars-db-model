# Star Wars Blog Database Model

> A SQLAlchemy-based database model for a Star Wars blog application, featuring user management, characters, planets, and favorites. This project demonstrates database modeling and relationships using SQLAlchemy.

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

- Star Wars themed database model
- User management
- Character and Planet information
- Favorites system
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

## Project Structure

```
/
├── src/
│   ├── models.py        # Database models and diagram generation
│   ├── app.py          # API endpoints
│   └── utils.py        # Utility functions
├── scripts/
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

## Database Models

The project includes four main models:

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
       homeworld_id: Mapped[int] = mapped_column(ForeignKey("planets.id"))
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
       user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
       character_id: Mapped[int] = mapped_column(ForeignKey("characters.id"))
       planet_id: Mapped[int] = mapped_column(ForeignKey("planets.id"))
       created_at: Mapped[datetime] = mapped_column(DateTime)
   ```

## Generating the Database Diagram

You can generate the database diagram using:

```sh
pipenv run diagram
```

This will generate a `diagram.txt` file in the root directory with the complete database schema.

## Development

This project demonstrates:
- Database modeling with SQLAlchemy
- Entity relationships and foreign keys
- Database diagram generation
- Flask integration with SQLAlchemy

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**Dante Fasano** - [GitHub](https://github.com/dantefasano)

Project Link: [https://github.com/dantefasano/starwars-db-model](https://github.com/dantefasano/starwars-db-model)

---

Made with ❤️ by Dante Fasano
