import json
from bson import json_util
import re
import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

# read file
with open('complex.json', 'r') as myfile:
    data=myfile.read()

s = json.dumps(data, default=json_util.default)
j = json.loads(s)

r = re.sub("\/\*.*\*\/",'',j)
r = re.sub("ObjectId\(",'',r)
r = re.sub("NumberLong\(",'',r)
r = re.sub("\)",'',r)
r = re.sub("{\n    \"_id\"",",{\n    \"_id\"",r)
r = r.strip()
r = r[1:]
r = '['+r+']'

cpx = json.loads(r)
#print(cpx)

for x in cpx:
    _id = x.get('_id')
    category = x.get('category') if x.get('category') is not None else 'XXXXX'
    name = x.get('name') if x.get('name') is not None else 'XXXXX'
    developer_name = x.get('developer_name')
    address_street = x.get('address_street')
    address_city = x.get('address_city')
    address_subdistrict = x.get('address_subdistrict')
    address_urban = x.get('address_urban')
    address_province = x.get('address_province')
    address_zip = x.get('address_zip')
    address_coordinate = x.get('address_coordinate')
    
    #convert facilities to string
    facilities = x.get('facilities') #need breakdown
    temp_facilities = []
    
    for key, value in facilities.items():
        aKey = key
        aValue = value
        if aValue == True :
            temp_facilities.append(aKey)
    
    facilities = ','.join(str(e) for e in temp_facilities)
    #############################################
    
    #breakdown images
    images = x.get('images') #need breakdown
    images_interior = images.get('images_interior')
    if(images_interior is not None):
        for item in images_interior:
            url = item.get('url')
            alternate_text = item.get('alternate_text')
            priority = item.get('priority')
            insertImages = "INSERT INTO complex_images (_id, category_images, source, url, alternate_text, priority)"
            insertImages += "values (%s,%s,%s,%s,%s,%s)"
            insertValue = (_id,'images_interior', 'complex', url, alternate_text, priority) 
            mycursor.execute(insertImages, insertValue)
        #mydb.commit()
            
    images_exterior = images.get('images_exterior')
    if(images_exterior is not None):
        for item in images_exterior:
            url = item.get('url')
            alternate_text = item.get('alternate_text')
            priority = item.get('priority')
            insertImages = "INSERT INTO complex_images (_id, category_images, source ,url, alternate_text, priority)"
            insertImages += "values (%s,%s,%s,%s,%s,%s)"
            insertValue = (_id,'images_exterior', 'complex',url, alternate_text, priority) 
            mycursor.execute(insertImages, insertValue)
        #mydb.commit()
            
    images_floorplan = images.get('images_floorplan')
    if(images_floorplan is not None):
        for item in images_floorplan:
            url = item.get('url')
            alternate_text = item.get('alternate_text')
            priority = item.get('priority')
            insertImages = "INSERT INTO complex_images (_id, category_images, source, url, alternate_text, priority)"
            insertImages += "values (%s,%s,%s,%s,%s,%s)"
            insertValue = (_id,'images_floorplan', 'complex', url, alternate_text, priority) 
            mycursor.execute(insertImages, insertValue)
        #mydb.commit()
    
    images_360 = images.get('images_360')
    if(images_360 is not None):
        for item in images_360:
            url = item.get('url')
            alternate_text = item.get('alternate_text')
            priority = item.get('priority')
            insertImages = "INSERT INTO complex_images (_id, category_images, source, url, alternate_text, priority)"
            insertImages += "values (%s,%s,%s,%s,%s,%s)"
            insertValue = (_id,'images_360', 'complex', url, alternate_text, priority) 
            mycursor.execute(insertImages, insertValue)
    
    images_developer = images.get('images_developer')
    if(images_developer is not None):
        for item in images_developer:
            url = item.get('url')
            alternate_text = item.get('alternate_text')
            priority = item.get('priority')
            insertImages = "INSERT INTO complex_images (_id, category_images, source, url, alternate_text, priority)"
            insertImages += "values (%s,%s,%s,%s,%s,%s)"
            insertValue = (_id,'images_developer', 'complex', url, alternate_text, priority) 
            mycursor.execute(insertImages, insertValue)
            
    images_banner = images.get('images_banner')
    if(images_banner is not None):
        for item in images_banner:
            url = item.get('url')
            alternate_text = item.get('alternate_text')
            priority = item.get('priority')
            insertImages = "INSERT INTO complex_images (_id, category_images, source, url, alternate_text, priority)"
            insertImages += "values (%s,%s,%s,%s,%s,%s)"
            insertValue = (_id,'images_banner', 'complex', url, alternate_text, priority) 
            mycursor.execute(insertImages, insertValue)
    
    images_brochure = images.get('images_brochure')
    if(images_brochure is not None):
        for item in images_brochure:
            url = item.get('url')
            alternate_text = item.get('alternate_text')
            priority = item.get('priority')
            insertImages = "INSERT INTO complex_images (_id, category_images, source, url, alternate_text, priority)"
            insertImages += "values (%s,%s,%s,%s,%s,%s)"
            insertValue = (_id,'images_brochure', 'complex', url, alternate_text, priority) 
            mycursor.execute(insertImages, insertValue)
    
    video_link = images.get('video_link')
    if(video_link is not None):
        for item in video_link:
            url = item.get('url')
            alternate_text = item.get('alternate_text')
            priority = item.get('priority')
            insertImages = "INSERT INTO complex_images (_id, category_images, source, url, alternate_text, priority)"
            insertImages += "values (%s,%s,%s,%s,%s,%s)"
            insertValue = (_id,'video_link', 'complex', url, alternate_text, priority) 
            mycursor.execute(insertImages, insertValue)
    
    ################################################
    id = x.get('id')
    tower_total = x.get('tower_total')
    
    # convert branches to string
    branches = x.get('branches')
    temp_branch = []
    
    for key, value in branches.items():
        aKey = key
        aValue = value
        if aValue == True :
            temp_branch.append(aKey)
            
    branches = ','.join(str(e) for e in temp_branch)
    ############################################
    unit_rent_total = x.get('unit_rent_total')
    unit_sell_total = x.get('unit_sell_total')
    address_country = x.get('address_country')
    developer_legal_name = x.get('developer_legal_name')
    land_size = x.get('land_size')
    last_update_at = datetime.datetime.fromtimestamp(x.get('last_update_at') / 1e3) 
    last_update_by_uid = x.get('last_update_by_uid')
    
    # convert surrounding_area to string
    surrounding_area = x.get('surrounding_area') #need breakdown
    temp_surrounding_area = []
    
    for key, value in surrounding_area.items():
        aKey = key
        aValue = value
        if aValue == True :
            temp_surrounding_area.append(aKey)
            
    surrounding_area = ','.join(str(e) for e in temp_surrounding_area)
    
    #################################################
    #convert address area to string
    address_area = x.get('address_area')
    temp_address_area = []
    
    for key, value in address_area.items():
        aKey = key
        aValue = value
        if aValue == True :
            temp_address_area.append(aKey)
    
    address_area = ','.join(str(e) for e in temp_address_area)
    
    ################################################
    create_at = x.get('create_at')
    create_by_uid = x.get('create_by_uid')
    status = x.get('status') if x.get('status') is not None else 0
    code = x.get('code')
    
    #convert service type to string
    service_types = x.get('service_types')
    service_types = ','.join(str(e) for e in service_types)
    ######################################################
    
    
    print(_id)
    
    sql2 = "INSERT INTO complex (_id, category, name, developer_name, address_street, address_city, address_subdistrict"
    sql2 += ", address_urban, address_province, address_zip, address_coordinate, id, tower_total, unit_rent_total"
    sql2 += ", unit_sell_total, address_country, developer_legal_name, land_size, last_update_at, last_update_by_uid"
    sql2 += ", surrounding_area, address_area, create_by_uid, status, code, service_types, facilities, branches)"
    sql2 += " values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val2 = (_id, category, name, developer_name, address_street, address_city, address_subdistrict, address_urban
            , address_province, address_zip, address_coordinate, id, tower_total, unit_rent_total, unit_sell_total
            , address_country, developer_legal_name, land_size, last_update_at, last_update_by_uid, surrounding_area
            , address_area, create_by_uid, status, code, service_types, facilities, branches)
    mycursor.execute(sql2, val2)
    mydb.commit()
    

