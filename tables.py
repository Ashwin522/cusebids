from app import app, db

# Create the application context
with app.app_context():
    # Create all tables in the database
    db.create_all()