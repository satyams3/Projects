# import required modules
import mysql.connector

# create connection object
con = mysql.connector.connect(
    host="127.0.0.1", user="myname",
    password="mytestpass", database="test_dbschema")

# create cursor object
cursor = con.cursor()

# assign data query
query1 = "desc test_table"

# executing cursor
cursor.execute(query1)

# display all records
table = cursor.fetchall()

# describe table
print('\n Table Description:')
for attr in table:
    print(attr)

# assign data query
query2 = "select * from test_table"

# executing cursor
cursor.execute(query2)

# display all records
table = cursor.fetchall()

# fetch all columns
print('\n Table Data:')
for row in table:
    print(row[0], end=" ")
    print(row[1], end=" ")
    print(row[2], end=" ")
    print(row[3], end="\n")

# closing cursor connection
cursor.close()

# closing connection object
con.close()
