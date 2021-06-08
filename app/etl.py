"""
etl.py
Extract, transform, and load functions and classes for the back-end
"""
import pymongo
import datetime
import pytz
import os

def process(form):
    return {'firstName': form.firstName.data,
            'lastName' : form.lastName.data,
            'organization' : form.organization.data,
            'email' : form.email.data,
            'phone' : form.phone.data,
            'goods' : form.goods.data if (form.goods.data != None) else [],
            'otherGoods' : form.otherGoods.data,
            'labor' : form.labor.data if (form.labor.data != None) else [],
            'otherLabor' : form.otherLabor.data,
            'cityLocation' : form.cityLocation.data,
            'regionLocation' : form.regionLocation.data,
            'countryLocation' : form.countryLocation.data,
            'description' : form.description.data}  

def generateTimeData(doc):
    coTime = pytz.timezone('US/Mountain')
    time = coTime.localize(datetime.datetime.now())
    doc['timestamp'] = time.timestamp()
    doc['datetime'] = time.strftime('%d %h %Y %H:%M:%S')
    return doc

def prepareDoc(doc):
    display = {}
    keys = ['organization', 'goods', 'labor', 'description']
    for k in keys:
        display[k] = doc[k]
    # Check if there is a valid region location
    if doc['regionLocation']:
        display['location'] = str(doc['cityLocation']+', '+doc['countryLocation'])
    else:
        display['location'] = str(doc['cityLocation']+', '+doc['regionLocation']+', '+doc['countryLocation'])
    # Append other goods and other labor
    if doc['otherGoods']: display['goods'].append(doc['otherGoods'])
    if doc['otherLabor']: display['labor'].append(doc['otherLabor'])
    return display

def writePledge(doc):
    client = pymongo.MongoClient('mongodb+srv://username:password@database_url') # Insert credentials for MongoDB Atlas
    db = client['covid-19-se']
    doc = generateTimeData(doc)
    db.pledges.insert_one(doc)
    client.close()
    del client

def writeRequest(doc):
    client = pymongo.MongoClient('mongodb+srv://username:password@database_url') # Insert credentials for MongoDB Atlas
    db = client['covid-19-se']
    doc = generateTimeData(doc)
    db.requests.insert_one(doc)
    client.close()
    del client

# Get all requested orders sorted by newest
def getRequests():
    client = pymongo.MongoClient('mongodb+srv://username:password@database_url') # Insert credentials for MongoDB Atlas
    # Descending timestamps sorts requests from newest to oldest
    cursor = client['covid-19-se'].requests.find().sort('timestamp', pymongo.DESCENDING)
    requests = []
    for doc in cursor:
        requests.append(prepareDoc(doc))
    client.close()
    del client
    return requests

