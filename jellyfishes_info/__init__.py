from importlib import import_module
from settings import LANGUAGES, RISK_LEVELS, ABUNDANCE_RATIOS


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
