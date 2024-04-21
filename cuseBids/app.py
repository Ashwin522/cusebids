from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # Handle login form submission here
    email = request.form['email']
    password = request.form['password']
    # Add your login logic here
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    # Handle register form submission here
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']
    # Add your registration logic here
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
