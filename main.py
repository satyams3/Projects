
import mysql.connector


con = mysql.connector.connect(
    host="127.0.0.1", user="myname", port="3306",
    password="mytestpass", database="test_dbschema")


cursor = con.cursor()


query1 = "select * from teat_table"


cursor.execute(query2)


table = cursor.fetchall()


print('\n Table Data:')
for row in table:
    print(row[0], end=" ")
    print(row[1], end=" ")
    print(row[2], end=" ")
    print(row[3], end="\n")


cursor.close()


con.close()
