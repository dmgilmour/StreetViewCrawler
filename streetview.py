import requests
#url = 'https://maps.googleapis.com/maps/api/streetview/metadata?'
url = 'https://maps.googleapis.com/maps/api/streetview/metadata?location=44.256389,52.006111&key=AIzaSyBBRWBs4PgdqYyUGpuy-EUiejloKBrC7NQ'

print(requests.get(url))
