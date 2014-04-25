from bottle import template, abort, run, response, Bottle
from jellyfishes_info import jellyfish_info
from api import MedJellyAPI
import settings

app = Bottle()

@app.get('/<lang>/<beach:path>')
def api(lang, beach):
    jellyfishes = []

    if lang not in settings.LANGUAGES:
        abort(400, "Invalid language code: %s" % lang)
    if beach not in settings.BEACHES:
        abort(404, "Beach %s is not found" % beach)

    jelly_risk = MedJellyAPI.jellyfishes_by_beach(settings.BEACHES[beach])
    for jelly in jelly_risk:
        jellyfishes.append(jellyfish_info(lang, jelly))

    response.set_header("Access-Control-Allow-Origin", "*")
    return {'jellyfishes': jellyfishes}


if __name__ == "__main__":
    run(host='localhost', app=app, port=8080, debug=True, reloader=True)
