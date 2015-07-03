from importlib import import_module
from settings import LANGUAGES, RISK_LEVELS, ABUNDANCE_RATIOS,CARTODB_URL,API_KEY,BEACHES_LONG_LAT,BEACHES
from api import jellyfishes_by_beach
import requests
import datetime

JELLYFISHES = {}
for lang in LANGUAGES:
    JELLYFISHES[lang] = import_module('jellyfishes_info.%s.jellyfishes' % lang).JELLYFISHES


def jellyfish_info(lang, jellyfish):
    jellyfish_id = jellyfish['jellyFishId']
    risk_level = jellyfish['status']
    abundance = jellyfish['abundance']
    jelly = JELLYFISHES[lang][jellyfish_id]
    risk_description = jelly['risk_description'][risk_level] % {
        "abundance": abundance,
        "abundance_ratio": ABUNDANCE_RATIOS[lang][abundance]
    }

    return {
        'scientific_name': jelly['scientific_name'],
        'common_name': jelly['common_name'],
        "photo": jelly['photo'],
        "risk_level": RISK_LEVELS[risk_level][lang],
        "description": jelly['description'] + risk_description
    }

def meduses_catalunya(lang):
    jellyfishes_info = {}
    for beach in (BEACHES):
        jellyfishes_info[beach] = {'jellyfishes':[]}
        jellyfishes_info[beach] = {'id_beach':BEACHES[beach]}
        jellyfishes_info[beach]['jellyfishes'] = jellyfishes_by_beach(BEACHES[beach],lang)
    return jellyfishes_info

def beaches_catalunya(lang):
    beaches = {}
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    day_after_tomorrow = today + datetime.timedelta(days=2)
    table = 'pred_pelagia'
    sql = "select prob,lat,lon,date from "+table+" WHERE date in( '"+str(today)+"','"+str(tomorrow)+"','"+str(day_after_tomorrow)+"') &api_key="+API_KEY+" ORDER BY date "
    r = requests.get(CARTODB_URL + sql)
    r.raise_for_status()
    data = r.json()
    
    for i,beach in enumerate(BEACHES):
        for d in data['rows']:
            coord = BEACHES_LONG_LAT[BEACHES[beach]].split(",")
            d1 = datetime.datetime.strptime(d['date'], '%Y-%m-%dT%H:%M:%SZ')
            if d1.strftime("%Y-%m-%d") == today.strftime("%Y-%m-%d"):
                if (d['lat'] == float(coord[1])) and (d['lon'] == float(coord[0])):
                    beaches[beach] = {'jellyfish':[]}
                    beaches[beach]['jellyfish'].append({'scientific_name':'pelagia'})
                    beaches[beach]['jellyfish'].append({'bloom_today':d['prob']})
            
            elif d1.strftime("%Y-%m-%d") == tomorrow.strftime("%Y-%m-%d"):
                if (d['lat'] == float(coord[1])) and (d['lon'] == float(coord[0])):
                    beaches[beach]['jellyfish'].append({"bloom_tomorrow":d['prob']})
            
            elif d1.strftime("%Y-%m-%d") == day_after_tomorrow.strftime("%Y-%m-%d"):
                if (d['lat'] == float(coord[1])) and (d['lon'] == float(coord[0])):
                    beaches[beach]['jellyfish'].append({"bloom_after_tomorrow":d['prob']})
    
    return beaches