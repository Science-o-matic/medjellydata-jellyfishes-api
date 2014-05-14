from es_ES import jellyfishes as jellyfishes_es_ES
from ca_ES import jellyfishes as jellyfishes_ca_ES
from en_EN import jellyfishes as jellyfishes_en_EN
from settings import RISK_LEVELS


JELLYFISHES = {
    'es_ES': jellyfishes_es_ES.JELLYFISHES,
    'ca_ES': jellyfishes_ca_ES.JELLYFISHES,
    'en_EN': jellyfishes_en_EN.JELLYFISHES,
}


def jellyfish_info(lang, jellyfish):
    jellyfish_id = jellyfish['id']
    risk_level = jellyfish['status']
    jelly = JELLYFISHES[lang][jellyfish_id]

    return {
        'scientific_name': jelly['scientific_name'],
        'common_name': jelly['common_name'],
        "photo": jelly['photo'],
        "risk_level": RISK_LEVELS[risk_level][lang],
        "description": jelly['description'] +
        jelly['risk_description'][risk_level]
        }
