import MySQLdb

# connection details
host = "localhost"
user = "your_username"
password = "your_password"
database = "your_database"

# connect to the database
db = MySQLdb.connect(host=host, user=user, passwd=password, db=database)

# print the connection details
print("Connected to database: {}".format(database))
print("Host: {}".format(host))
print("User: {}".format(user))
print("Password: {}".format(password))

# close the database connection
db.close()

