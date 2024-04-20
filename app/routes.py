import os
from flask import render_template, request, jsonify
from . import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Get the base directory of the current module (app directory)
base_dir = os.path.abspath(os.path.dirname(__file__))

# Specify the path to the SQLite database relative to the current file
db_path = os.path.join(os.path.dirname(__file__), 'data', 'ratings.db')

# Configure SQLAlchemy to use the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking (optional)

db = SQLAlchemy(app)

# Create all database tables based on defined models
with app.app_context():
    db.create_all()

migrate = Migrate(app, db)

# Define a model for photo ratings
class PhotoRating(db.Model):
    __tablename__ = 'photo_rating'

    id = db.Column(db.Integer, primary_key=True)
    photo_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<PhotoRating photo_id={self.photo_id}, rating={self.rating}>'
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_rating', methods=['POST'])
def save_rating():
    data = request.get_json()
    photo_id = data['photo_id']
    rating = data['rating']

    # Create a new PhotoRating object and add it to the database
    photo_rating = PhotoRating(photo_id=photo_id, rating=rating)
    db.session.add(photo_rating)
    db.session.commit()

    return jsonify({'message': f'Rating {rating} saved for Photo {photo_id}'})