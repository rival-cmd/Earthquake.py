
import urllib3, certifi, json
from datetime import datetime

def printResults(data):
    JSON = json.loads(data)
    if "title" in JSON['metadata']:
        print(JSON['metadata']['title'])

    if "count" in JSON['metadata']:
        print(str(JSON['metadata']['count']) + ' Events Recorded This Hour' + '\n')

    for i in JSON['features']:
        epoch = int(i['properties']['time']) / 1000
        print (datetime.utcfromtimestamp(epoch).strftime('%m-%d-%Y %H:%M:%S') + ' UTF')
        print(i['properties']['place'] + '    Magnitude: ' + str(i['properties']['mag']))
        print('Longitude: ' + str(i['geometry']['coordinates'][0]) + '  Latitude: ' + str(i['geometry']['coordinates'][1]) + '  Depth: ' + str(i['geometry']['coordinates'][2]) + '\n')

def main():
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())

    request = http.request('GET', "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson")
    
    print('URL Code: ' + str(request.status))
    if request.status == 200:
        data = request.data
        printResults(data)
    else:
        print ('Response Code: {}  : Failed to Parse Webpage'.format(request.status))
    

if __name__ == "__main__":
    main()