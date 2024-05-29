import requests
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"
loc1 = "Santiago, Chile"
loc2 = "Ovalle, Chile"
key = "e635c0d0-8b5a-43cd-96ad-a527b8f84484" # Reemplazar con su clave de API de Graphhopper

url = geocode_url + urllib.parse.urlencode ({"q": loc1, "limit": "1", "key": key})

replydata = requests.get(url)
json_data = replydata.json()
json_status = replydata.status_code
print (json_data)
