#from xml.dom import minidom
from bs4 import BeautifulSoup
import simplejson
import csv
print "Reading input ..."
#xmldoc = minidom.parse("timhortons.xml")
#markers = xmldoc.getElementsByTagName('markers')
with open("timhortons.xml","r") as f:
    html = f.read()
soup = BeautifulSoup(html)
#exit()
markers = soup.findAll("marker")
stores = []
print "Writing output ..."
for marker in markers:
    store = {
      'markerid': marker['id'],
      'storeid': marker['storeid'],
      'street': marker['address2'],
      'city': marker['city'],
      'state': marker['province'],
      'lat': marker['lat'],
      'lng': marker['lng'],
      'zipcode': marker['postal'],
    }
    stores.append(store)
with open("timhortons.json","w") as f:
    f.write(simplejson.dumps(stores))

with open("timhortons.csv","w") as f:
    writer = csv.writer(f,delimiter=',', quotechar='"')
    writer.writerow("markerid,storeid,street,city,state,lat,lng,zipcode,")
    for store in stores:
        row = [store['markerid'].encode('utf-8'),
               store['storeid'].encode('utf-8'),
               store['street'].encode('utf-8'),
               store['city'].encode('utf-8'),
               store['state'].encode('utf-8'),
               store['lat'].encode('utf-8'),
               store['lng'].encode('utf-8'),
               store['zipcode'].encode('utf-8'),
              ]
        writer.writerow(row)
print "Done."
