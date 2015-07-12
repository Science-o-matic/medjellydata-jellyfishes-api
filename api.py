import os
import settings
import random
import requests
import datetime
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

    print url
    r = requests.get(url, headers=headers)
    r.raise_for_status()

    return r.json()["jellyFishesHazard"]

def pelagia_bloom(beach_id):
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    day_after_tomorrow = today + datetime.timedelta(days=2)
    coord = settings.BEACHES_LONG_LAT[beach_id].split(",")
    sql = "select prob,date from pred_pelagia WHERE date in( '"+str(today)+"','"+str(tomorrow)+"','"+str(day_after_tomorrow)+"')AND lat="+coord[1]+" AND lon = "+coord[0]+"&api_key="+settings.API_KEY
    r = requests.get(settings.CARTODB_URL + sql)
    r.raise_for_status()
    data = r.json()
    probabilities = []
    for d in data['rows']:
        d1 = datetime.datetime.strptime(d['date'], '%Y-%m-%dT%H:%M:%SZ')
        if d1.strftime("%Y-%m-%d") == today.strftime("%Y-%m-%d"):
            probabilities.append(d['prob'])
        elif d1.strftime("%Y-%m-%d") == tomorrow.strftime("%Y-%m-%d"):
            probabilities.append(d['prob'])
        elif d1.strftime("%Y-%m-%d") == day_after_tomorrow.strftime("%Y-%m-%d"):
            probabilities.append(d['prob'])
    return probabilities
