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
with open('tower.json', 'r') as myfile:
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

#f = open("testfile12.json", "w")
#f.write(r)
#f.close()

for x in cpx:
    _id = x.get('_id')
    complex_id = x.get('complex_id')
    create_by_id = x.get('create_by_id')
    last_update_at = datetime.datetime.fromtimestamp(x.get('last_update_at') / 1e3)
    category = x.get('category') if x.get('category') is not None else 'XXXXX'
    name = x.get('name') if x.get('name') is not None else 'XXXXX'
    year_completion = x.get('year_completion')
    year_renovation = x.get('year_renovation')
    floor_count = x.get('floor_count')
    description = x.get('description') if x.get('description') is None else x.get('description').get('id')
    parking = json.dumps(x.get('parking'))
    lift = json.dumps(x.get('lift'))
    
    # convert surrounding_area to string
    internet = x.get('internet')
    temp_internet = []
    
    if(internet is not None and internet != {}):
        for key, value in internet.items():
            aKey = key
            aValue = value
            if aValue == True :
                temp_internet.append(aKey)
            internet = ','.join(str(e) for e in temp_internet)
    else:
        internet = None
   
    
    #################################### 
    
    unit_total = x.get('unit_total')
    id = x.get('id')
    
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
    architect = x.get('architect')
    certificate = x.get('certificate')
    contractor = x.get('contractor')
    fee_component = json.dumps(x.get('fee_component'))
    last_update_by_uid = x.get('last_update_by_uid')
    promo = x.get('promo')
    rent_commission = x.get('rent_commission')
    sell_commission = x.get('sell_commission')
    year_completed_estimation = x.get('year_completed_estimation')
    year_construction = x.get('year_construction')
    
    #convert building_type to string
    building_type = x.get('building_type')
    building_type = ','.join(str(e) for e in building_type)
    ######################################################
    
    service_charge = x.get('service_charge')
    auto_description = x.get('auto_description')
    is_leads_agent = x.get('is_leads_agent')
    average_floor_plate = x.get('average_floor_plate')
    ceiling_height = x.get('ceiling_height')
    commercial_terms = x.get('commercial_terms')
    condition = x.get('condition')
    electricity = x.get('electricity')
    fire_safety = x.get('fire_safety')
    grade = x.get('grade')
    land_size = x.get('land_size')
    max_zone_per_floor = x.get('max_zone_per_floor')
    office_hours = x.get('office_hours')
    power_line = x.get('power_line')
    selling_point = json.dumps(x.get('selling_point'))
    semi_gross_area = x.get('semi_gross_area')
    sinking_fund = x.get('sinking_fund')
    complex = json.dumps(x.get('complex'))
    create_at = x.get('create_at') if x.get('create_at') is None else datetime.datetime.fromtimestamp(x.get('create_at') / 1e3) 
    status = x.get('status') if x.get('status') is not None else 0
    
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
            insertValue = (_id,'images_interior', 'tower', url, alternate_text, priority) 
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
            insertValue = (_id,'images_exterior', 'tower',url, alternate_text, priority) 
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
            insertValue = (_id,'images_floorplan', 'tower', url, alternate_text, priority) 
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
            insertValue = (_id,'images_360', 'tower', url, alternate_text, priority) 
            mycursor.execute(insertImages, insertValue)
    
    images_developer = images.get('images_developer')
    if(images_developer is not None):
        for item in images_developer:
            url = item.get('url')
            alternate_text = item.get('alternate_text')
            priority = item.get('priority')
            insertImages = "INSERT INTO complex_images (_id, category_images, source, url, alternate_text, priority)"
            insertImages += "values (%s,%s,%s,%s,%s,%s)"
            insertValue = (_id,'images_developer', 'tower', url, alternate_text, priority) 
            mycursor.execute(insertImages, insertValue)
            
    images_banner = images.get('images_banner')
    if(images_banner is not None):
        for item in images_banner:
            url = item.get('url')
            alternate_text = item.get('alternate_text')
            priority = item.get('priority')
            insertImages = "INSERT INTO complex_images (_id, category_images, source, url, alternate_text, priority)"
            insertImages += "values (%s,%s,%s,%s,%s,%s)"
            insertValue = (_id,'images_banner', 'tower', url, alternate_text, priority) 
            mycursor.execute(insertImages, insertValue)
    
    images_brochure = images.get('images_brochure')
    if(images_brochure is not None):
        for item in images_brochure:
            url = item.get('url')
            alternate_text = item.get('alternate_text')
            priority = item.get('priority')
            insertImages = "INSERT INTO complex_images (_id, category_images, source, url, alternate_text, priority)"
            insertImages += "values (%s,%s,%s,%s,%s,%s)"
            insertValue = (_id,'images_brochure', 'tower', url, alternate_text, priority) 
            mycursor.execute(insertImages, insertValue)
    
    video_link = images.get('video_link')
    if(video_link is not None):
        for item in video_link:
            url = item.get('url')
            alternate_text = item.get('alternate_text')
            priority = item.get('priority')
            insertImages = "INSERT INTO complex_images (_id, category_images, source, url, alternate_text, priority)"
            insertImages += "values (%s,%s,%s,%s,%s,%s)"
            insertValue = (_id,'video_link', 'tower', url, alternate_text, priority) 
            mycursor.execute(insertImages, insertValue)
    ##############################################
        
    print(_id)
    #print(internet)
    
    sql2 = "INSERT INTO tower (_id, complex_id, create_by_id, last_update_at, category, name, year_completion"
    sql2 += ", year_renovation, floor_count, description, parking, lift, internet, unit_total, id, branches, unit_rent_total"
    sql2 += ", unit_sell_total, architect, certificate, contractor, fee_component, last_update_by_uid"
    sql2 += ", promo, rent_commission, sell_commission, year_completed_estimation, year_construction, building_type, service_charge"
    sql2 += ",auto_description, is_leads_agent, average_floor_plate, ceiling_height, commercial_terms, condition1, electricity"
    sql2 += ",fire_safety, grade, land_size, max_zone_per_floor, office_hours, power_line, selling_point, semi_gross_area"
    sql2 += ",sinking_fund, complex, create_at, status)"
    sql2 += " values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val2 = (_id, complex_id, create_by_id, last_update_at, category, name, year_completion, year_renovation, floor_count
            , description, parking, lift, internet, unit_total, id, branches, unit_rent_total, unit_sell_total, architect, certificate
            , contractor, fee_component, last_update_by_uid, promo, rent_commission, sell_commission, year_completed_estimation
            , year_construction, building_type, service_charge,auto_description, is_leads_agent, average_floor_plate, ceiling_height
            , commercial_terms, condition, electricity,fire_safety, grade, land_size, max_zone_per_floor, office_hours, power_line
            , selling_point, semi_gross_area,sinking_fund, complex, create_at, status)
    mycursor.execute(sql2, val2)
    mydb.commit()