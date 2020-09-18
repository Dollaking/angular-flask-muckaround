import pymongo

# Connection to the database
my_client = pymongo.MongoClient("mongodb://localhost:27017/")

# Our database
my_db = my_client["angular-flask-muckaround"]

# Our collection
my_collection = my_db["people"]

# Our entry that we will insert
my_entry = { "name": "Joe", "colour": "Blue" }


# Inserting an item
x = my_collection.insert_one(my_entry)

# Printing the inserted _id
print("Inserted id is", x.inserted_id)

# Finding the first inserted item
print("First inserted item is:")
print(my_collection.find_one())

# Finding all items in the collection
print("All entires are:")
for x in my_collection.find():
    print(x)
