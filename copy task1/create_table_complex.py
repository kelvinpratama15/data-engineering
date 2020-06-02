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

strDropTable = "DROP TABLE IF EXISTS complex"
mycursor.execute(strDropTable)

strCreateTable = "CREATE TABLE IF NOT EXISTS complex ("
strCreateTable += "_id VARCHAR(255) PRIMARY KEY,"
strCreateTable += "category VARCHAR(255) NOT NULL,"
strCreateTable += "name VARCHAR(255) NOT NULL,"
strCreateTable += "developer_name VARCHAR(255),"
strCreateTable += "address_street VARCHAR(255),"
strCreateTable += "address_city VARCHAR(255),"
strCreateTable += "address_subdistrict VARCHAR(255),"
strCreateTable += "address_urban VARCHAR(255),"
strCreateTable += "address_province VARCHAR(255),"
strCreateTable += "address_zip VARCHAR(255),"
strCreateTable += "address_coordinate VARCHAR(255),"
strCreateTable += "facilities TEXT,"
strCreateTable += "images TEXT,"
strCreateTable += "id VARCHAR(255),"
strCreateTable += "tower_total INT,"
strCreateTable += "branches TEXT(255),"
strCreateTable += "unit_rent_total INT,"
strCreateTable += "unit_sell_total INT,"
strCreateTable += "address_country TEXT,"
strCreateTable += "developer_legal_name VARCHAR(255),"
strCreateTable += "land_size DECIMAL(5,2),"
strCreateTable += "last_update_at DATETIME,"
strCreateTable += "last_update_by_uid VARCHAR(255),"
strCreateTable += "surrounding_area TEXT,"
strCreateTable += "address_area VARCHAR(255),"
strCreateTable += "create_at DATETIME,"
strCreateTable += "create_by_uid VARCHAR(255),"
strCreateTable += "status BOOLEAN NOT NULL,"
strCreateTable += "code VARCHAR(255),"
strCreateTable += "service_types TEXT(255))"

mycursor.execute(strCreateTable)