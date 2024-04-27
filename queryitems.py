from app import app, db, Item

with app.app_context():
    # Query all items from the database
    items = Item.query.all()

    # Print information about each item
    for item in items:
        print(f"Item ID: {item.id}")
        print(f"Name: {item.name}")
        print(f"Description: {item.description}")
        print(f"Starting Bid: {item.starting_bid}")
        print()
