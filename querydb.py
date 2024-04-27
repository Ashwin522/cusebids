from app import app, User, db

# Create an application context
with app.app_context():
    # Query all users
    all_users = User.query.all()
    print("All Users:")
    for user in all_users:
        print(user.firstname, user.lastname, user.email)

    # Query a specific user by email
    email_to_query = input("Enter the email of the user you want to query: ")
    user = User.query.filter_by(email=email_to_query).first()
    if user:
        print("User Found:")
        print(user.firstname, user.lastname, user.email)
    else:
        print("User with email '{}' not found.".format(email_to_query))
