import os
import settings
import random
import requests
from base64 import b64encode


AUTH_TOKEN = b64encode("%s:%s" % (settings.MEDJELLY_API_USER, settings.MEDJELLY_API_PASSWORD))

def jellyfishes_by_beach(beach_id, lang):
    url = "%(base_url)s/beaches/beach/%(id)i/lang/%(lang)s/device/%(device)s" % (
        {'base_url': settings.MEDJELLY_API_BASE_URL,
         'id': beach_id,
         'lang': lang,
         'device': settings.DEVICE_ID,
         })
    headers = {"Authorization": "Basic %s" % AUTH_TOKEN}

    r = requests.get(url, headers=headers)
    r.raise_for_status()

    return r.json()["jellyFishesHazard"]

def bloom_probability(table,beach_id):
    coord = settings.BEACHES_LONG_LAT[beach_id].split(",")
    sql = "select prob from "+table+" WHERE date = 'NOW()' AND lat="+coord[1]+" AND lon = "+coord[0]+"&api_key="+settings.API_KEY
    r = requests.get(settings.CARTODB_URL + sql)
    r.raise_for_status()
    data = r.json()
    
    probability = ""
    if len(data['rows']) > 0:
        probability = data['rows'][0]['prob']
    return probability