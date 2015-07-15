from importlib import import_module
from settings import LANGUAGES, RISK_LEVELS, ABUNDANCE_RATIOS,CARTODB_URL,API_KEY,BEACHES_LONG_LAT,BEACHES
from api import jellyfishes_by_beach, pelagia_bloom
import requests
import datetime
import settings

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
    jellyfishes_info = []
    for jellyfish_id in JELLYFISHES[lang]:
        jellyfishes_info.append(JELLYFISHES[lang][jellyfish_id])
    return {'jellyfishes': jellyfishes_info}

def beaches_catalunya(lang, stdout=False):
    beaches = {}
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    day_after_tomorrow = today + datetime.timedelta(days=2)
    table = 'pred_pelagia'
    sql = "select prob,lat,lon,date from "+table+" WHERE date in( '"+str(today)+"','"+str(tomorrow)+"','"+str(day_after_tomorrow)+"') &api_key="+API_KEY+" ORDER BY date "
    r = requests.get(CARTODB_URL + sql)
    r.raise_for_status()
    data = r.json()

    for _, beach in enumerate(BEACHES):
        jellyfishes = []
        jellyfishesHazard = jellyfishes_by_beach(settings.BEACHES[beach], lang)
        for jelly in jellyfishesHazard:
            aux_jelly = jellyfish_info(lang, jelly)
            pelagia_blooms = pelagia_bloom(settings.BEACHES[beach])
            if pelagia_blooms:
                try:
                    aux_jelly["bloom_today"] = pelagia_blooms[0]
                except IndexError:
                    aux_jelly["bloom_today"] = "N/A"
                try:
                    aux_jelly["bloom_tomorrow"] = pelagia_blooms[1]
                except IndexError:
                    aux_jelly["bloom_tomorrow"] = "N/A"
                try:
                    aux_jelly["bloom_after_tomorrow"] = pelagia_blooms[2]
                except IndexError:
                    aux_jelly["bloom_after_tomorrow"] = "N/A"
            jellyfishes.append(aux_jelly)
        beaches[beach] = {"jellyfishes": jellyfishes}

    if stdout:
        print beaches

    return beaches
