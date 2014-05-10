import os
import settings
import random
import requests
import base64


def jellyfishes_by_beach(beach_id, lang):
    url = "%(base_url)s/beaches/beach/%(id)i/lang/%(lang)s/device/%(device)s" % (
        {'base_url': settings.MEDJELLY_API_BASE_URL,
         'id': beach_id,
         'lang': lang,
         'device': settings.DEVICE_ID,
         })
    headers = {"Authorization": "Basic %s" % _auth_token()}

    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()["jellyFishesHazard"]


def _auth_token():
    auth_string = "%s:%s" % (settings.MEDJELLY_API_USER, settings.MEDJELLY_API_PASSWORD)
    return base64.b64encode(auth_string)
