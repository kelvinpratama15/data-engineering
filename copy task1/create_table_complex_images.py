import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="mydatabase"
)

# print(mydb)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")

#mycursor.execute("SHOW DATABASES")

strDropTable = "DROP TABLE IF EXISTS complex_images"
mycursor.execute(strDropTable)

strCreateTable = "CREATE TABLE IF NOT EXISTS complex_images ("
strCreateTable += "_id VARCHAR(255),"
strCreateTable += "category_images VARCHAR(255),"
strCreateTable += "source VARCHAR(255),"
strCreateTable += "url VARCHAR(255),"
strCreateTable += "alternate_text VARCHAR(255),"
strCreateTable += "priority VARCHAR(255))"

mycursor.execute(strCreateTable)