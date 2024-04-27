from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Query the database for a user with the provided email
    user = User.query.filter_by(email=email).first()

    # Check if the user exists and the password is correct
    if user and user.password == password:
        # Successful login, redirect to the homepage
        return redirect(url_for('home'))
    else:
        # Invalid credentials, redirect back to the login page
        return redirect(url_for('index'))

@app.route('/register', methods=['POST'])
def register():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']

    # Check if the email is already registered
    if User.query.filter_by(email=email).first():
        # Email already exists, redirect back to the registration page
        return redirect(url_for('index'))

    # Create a new user and add it to the database
    new_user = User(firstname=firstname, lastname=lastname, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    # Redirect to the homepage after successful registration
    return redirect(url_for('home'))

@app.route('/home')
def home():
    # Render the homepage
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
