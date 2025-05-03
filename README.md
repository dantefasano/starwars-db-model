# Instagram Database Model

> A SQLAlchemy-based database model for an Instagram-like application, featuring user management, posts, comments, likes, and following relationships. This project demonstrates database modeling and relationships using SQLAlchemy.

[![Flask](https://img.shields.io/badge/Flask-3.0.2-green.svg)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-blue.svg)](https://www.sqlalchemy.org/)
[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Keywords:** Flask, SQLAlchemy, Database Modeling, Instagram Clone, Python, Backend Development

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

- Complete Instagram-like database model
- User management with profiles
- Post creation and management
- Comment system
- Like functionality
- Following relationships
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

The project includes five main models that follow the format:
```
TableName
-
column_name data_type constraints
```

1. **User Model**
   ```python
   class User(db.Model):
       id: Mapped[int] = mapped_column(primary_key=True)
       username: Mapped[str] = mapped_column(String(80), unique=True)
       email: Mapped[str] = mapped_column(String(120), unique=True)
       password: Mapped[str] = mapped_column(nullable=False)
       profile_picture: Mapped[str] = mapped_column(String(255))
       bio: Mapped[str] = mapped_column(Text)
       is_active: Mapped[bool] = mapped_column(Boolean())
       created_at: Mapped[datetime] = mapped_column(DateTime)
   ```

2. **Post Model**
   ```python
   class Post(db.Model):
       id: Mapped[int] = mapped_column(primary_key=True)
       user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
       image_url: Mapped[str] = mapped_column(String(255))
       caption: Mapped[str] = mapped_column(Text)
       created_at: Mapped[datetime] = mapped_column(DateTime)
   ```

3. **Comment Model**
   ```python
   class Comment(db.Model):
       id: Mapped[int] = mapped_column(primary_key=True)
       user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
       post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
       content: Mapped[str] = mapped_column(Text)
       created_at: Mapped[datetime] = mapped_column(DateTime)
   ```

4. **Like Model**
   ```python
   class Like(db.Model):
       id: Mapped[int] = mapped_column(primary_key=True)
       user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
       post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
       created_at: Mapped[datetime] = mapped_column(DateTime)
   ```

5. **Follow Model**
   ```python
   class Follow(db.Model):
       id: Mapped[int] = mapped_column(primary_key=True)
       follower_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
       followed_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
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

Project Link: [https://github.com/dantefasano/instagram-database-model](https://github.com/dantefasano/instagram-database-model)

---

Made with ❤️ by Dante Fasano
