import csv
from model import Buildings, Tenants, Sections
from db import db_session


"""
Функции присваивания значений
"""

def add_building(row):
    building = Buildings(street = row['street'], index = row['index'], function = row['function'],
    count_floors = row['count_floors'], sections = row['sections'])
    
    db_session.add(building)
    db_session.commit()

def add_tenant(row):
    tenant = Tenants(name = row['name'], email = row['email'], personal_phone = row['personal_phone'],
    commercial_phone = row['commercial_phone'], start_rent = row['start_rent'], end_rent = row['end_rent'])

    db_session.add(tenant)
    db_session.commit()

def add_section(row):
    section = Sections(building_id = row['building_id'], index = row['index'], floor = row['floor'],
    function = row['function'], area = row['area'], tenant_id = row['tenant_id'])

    db_session.add(section)
    db_session.commit()

"""
Функции чтения csv файла с переносом даты в базу
"""

def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
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


if __name__ == '__main__':
    read_csv('buildings.csv')
    read_csv('tenants.csv')
    read_csv('sections.csv')


