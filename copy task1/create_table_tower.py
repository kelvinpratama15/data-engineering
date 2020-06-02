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

strDropTable = "DROP TABLE IF EXISTS tower"
mycursor.execute(strDropTable)

strCreateTable = "CREATE TABLE IF NOT EXISTS tower ("
strCreateTable += "_id VARCHAR(255),"
strCreateTable += "complex_id VARCHAR(255),"
strCreateTable += "create_by_id VARCHAR(255),"
strCreateTable += "last_update_at DATETIME,"
strCreateTable += "category VARCHAR(255) NOT NULL,"
strCreateTable += "name VARCHAR(255) NOT NULL,"
strCreateTable += "year_completion INT,"
strCreateTable += "year_renovation INT(255),"
strCreateTable += "floor_count VARCHAR(255),"
strCreateTable += "description VARCHAR(255),"
strCreateTable += "parking TEXT,"
strCreateTable += "lift TEXT,"
strCreateTable += "internet TEXT,"
strCreateTable += "unit_total INT,"
strCreateTable += "id VARCHAR(255),"
strCreateTable += "branches TEXT,"
strCreateTable += "unit_rent_total INT,"
strCreateTable += "unit_sell_total INT,"
strCreateTable += "architect VARCHAR(255),"
strCreateTable += "certificate VARCHAR(255),"
strCreateTable += "contractor VARCHAR(255),"
strCreateTable += "fee_component TEXT,"
strCreateTable += "last_update_by_uid VARCHAR(255),"
strCreateTable += "promo VARCHAR(255),"
strCreateTable += "rent_commission INT,"
strCreateTable += "sell_commission INT,"
strCreateTable += "year_completed_estimation INT,"
strCreateTable += "year_construction INT,"
strCreateTable += "building_type TEXT,"
strCreateTable += "service_charge INT,"
strCreateTable += "auto_description BOOLEAN,"
strCreateTable += "is_leads_agent BOOLEAN,"
strCreateTable += "average_floor_plate INT,"
strCreateTable += "ceiling_height INT,"
strCreateTable += "commercial_terms VARCHAR(255),"
strCreateTable += "condition1 VARCHAR(255),"
strCreateTable += "electricity VARCHAR(255),"
strCreateTable += "fire_safety VARCHAR(255),"
strCreateTable += "grade VARCHAR(255),"
strCreateTable += "land_size INT,"
strCreateTable += "max_zone_per_floor INT,"
strCreateTable += "office_hours VARCHAR(255),"
strCreateTable += "power_line VARCHAR(255),"
strCreateTable += "selling_point TEXT,"
strCreateTable += "semi_gross_area INT,"
strCreateTable += "sinking_fund INT,"
strCreateTable += "complex TEXT,"
strCreateTable += "create_at DATETIME,"
strCreateTable += "status BOOLEAN NOT NULL)"

mycursor.execute(strCreateTable)
#print(strCreateTable)