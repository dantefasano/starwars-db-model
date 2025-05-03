import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy_schemadisplay import create_schema_graph
from src.models import db

def generate_diagram():
    # Create a Flask app
    app = Flask(__name__)
    
    # Get the absolute path for the database
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'instance', 'database.db')
    
    # Configure the SQLite database with absolute path
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the database
    db.init_app(app)
    
    with app.app_context():
        # Create the engine
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        
        # Create the graph
        graph = create_schema_graph(
            metadata=db.metadata,
            show_datatypes=True,
            show_indexes=True,
            rankdir='LR',
            concentrate=False,
            engine=engine
        )
        
        # Write the diagram to a file
        diagram_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'diagram.png')
        graph.write_png(diagram_path)
        print(f"Diagram generated successfully at: {diagram_path}")

if __name__ == '__main__':
    generate_diagram() 