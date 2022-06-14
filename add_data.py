import csv
from webapp.models import Buildings, Tenants, Sections
from webapp import db
from datetime import datetime

"""
Функции присваивания значений
"""

def add_building(row):
    building = Buildings(street = row['street'], index = row['index'],
    count_floors = row['count_floors'], photo = row['photo'])
    
    db.session.add(building)
    db.session.commit()

def add_tenant(row):
    tenant = Tenants(name = row['name'], email = row['email'], personal_phone = row['personal_phone'],
    commercial_phone = row['commercial_phone'], start_rent = datetime.strptime(row['start_rent'], '%d.%m.%Y'),
    end_rent = datetime.strptime(row['end_rent'], '%d.%m.%Y'))

    db.session.add(tenant)
    db.session.commit()

def add_section(row):
    section = Sections(building_id = row['building_id'], index = row['index'], floor = row['floor'],
    function = row['function'], area = row['area'], tenant_id = row['tenant_id'])

    db.session.add(section)
    db.session.commit()

"""
Функции чтения csv файла с переносом даты в базу
"""

def read_csv(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter = ';')
        if 'building' in filename:
            for row in reader:
                add_building(row)
        elif 'tenants' in filename:
            for row in reader:
                add_tenant(row)
        elif 'section' in filename:
            for row in reader:
                add_section(row)


coordinates_of_building = [
    {'id': '1', 'lat_coordinate': 55.06724978121969, 'lon_coordinate': 60.09825174136776},
    {'id': '2', 'lat_coordinate': 55.06714203245765, 'lon_coordinate': 60.09761337562222},
    {'id': '3', 'lat_coordinate': 55.06679723446101, 'lon_coordinate': 60.098171275097314},
    {'id': '4', 'lat_coordinate': 55.067787994017486, 'lon_coordinate': 60.09784012730405},
    {'id': '5', 'lat_coordinate': 55.067261568696836, 'lon_coordinate': 60.09649365837861}, 
    {'id': '6', 'lat_coordinate': 55.06759404865595, 'lon_coordinate': 60.09542613919065},
    {'id': '7', 'lat_coordinate': 55.06791421192026, 'lon_coordinate': 60.09595185215759}, 
    {'id': '8', 'lat_coordinate': 55.06768332520949, 'lon_coordinate': 60.09713202412411}, 
    {'id': '9', 'lat_coordinate': 55.06791421192026, 'lon_coordinate': 60.09681015904238}
]

def add_buildings_coordinates(list_coordinates):
    for coordinates in list_coordinates:
        building = db.session.query(Buildings).filter(Buildings.id == coordinates['id']).first()
        building.lat = coordinates['lat_coordinate']
        building.lon = coordinates['lon_coordinate']
        db.session.commit()



if __name__ == '__main__':
    # add_buildings_coordinates(coordinates_of_building)
    # read_csv('buildings.csv')
    # read_csv('tenants.csv')
    # read_csv('sections.csv')


