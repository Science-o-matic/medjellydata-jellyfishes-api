from bottle import template, abort, run, response, Bottle
from jellyfishes_info import jellyfish_info
from api import jellyfishes_by_beach
import settings

app = Bottle()

@app.get('/<lang>/<beach:path>')
def api(lang, beach):
    if lang not in settings.LANGUAGES:
        abort(400, "Invalid language code: %s" % lang)
    if beach not in settings.BEACHES:
        abort(404, "Beach %s is not found" % beach)

    jellyfishes = []
    #    jellyfishesHazard = jellyfishes_by_beach(settings.BEACHES[beach], lang)
    #for jelly in jellyfishesHazard:
    #    jellyfishes.append(jellyfish_info(lang, jelly))
    jellyfishes.append(
        jellyfish_info(lang,
                       {'jellyFishId': 1,
                        'status': "HIGH_WARNING",
                        'abundance': 3,
                        }))

    response.set_header("Access-Control-Allow-Origin", "*")
    return {'jellyfishes': jellyfishes}


if __name__ == "__main__":
    run(host='localhost', app=app, port=8081, debug=True, reloader=True)
