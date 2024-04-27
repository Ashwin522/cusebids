from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db  # Importing db from models.py

app = Flask(__name__)
# Specify different database URIs for different databases
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_BINDS'] = {'listing': 'sqlite:///listing.db'}

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

# Importing models after initializing db to avoid circular imports
from models import User, Item

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # Handle login logic here
    print("Login route reached")
    email = request.form['email']
    password = request.form['password']
    
    # Check if the email exists in the database
    user = User.query.filter_by(email=email).first()
    if user:
        # Check if the password matches
        if user.password == password:
            # Password matches, redirect to home page
            return redirect(url_for('home'))
    
    # If email or password is incorrect, redirect to login page with an error message
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        # Render the registration form
        return render_template('register.html')
    elif request.method == 'POST':
        # Handle registration logic here
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        # Register user
        new_user = User(firstname=firstname, lastname=lastname, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        # Redirect to login page after registration
        return redirect(url_for('index'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/list_item', methods=['POST'])
def list_item():
    if request.method == 'POST':
        # Retrieve data from the form
        item_name = request.form['item_name']
        description = request.form['description']
        starting_bid = request.form['starting_bid']

        # Create a new item object and add it to the database
        new_item = Item(name=item_name, description=description, starting_bid=starting_bid)
        db.session.add(new_item)
        db.session.commit()

        # Redirect to a success page or back to the account page
        return redirect(url_for('account'))

if __name__ == '__main__':
    app.run(debug=True)
