import os
from es_ES import jellyfishes
from settings import RISK_LEVELS


JELLYFISHES = {
    'es_ES': jellyfishes.JELLYFISHES,
}

def jellyfish_info(lang, jellyfish):
    jellyfish_id = jellyfish['id']
    risk_level = jellyfish['risk_level']
    jelly = JELLYFISHES['es_ES'][jellyfish_id]

    try:
        jelly['risk_description'][risk_level]
    except KeyError:
        risk_level = jelly['risk_description'].keys()[0]


    return {
        'scientific_name': jelly['scientific_name'],
        'common_name': jelly['common_name'],
        "photo": jelly['photo'],
        "risk_level": RISK_LEVELS[risk_level][lang],
        "description": jelly['description'] +
        jelly['risk_description'][risk_level]
        }
