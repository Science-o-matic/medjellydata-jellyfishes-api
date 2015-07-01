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
        if beach == "meduses_catalunya":
            meduses = meduses_catalunya(lang);
            response.set_header("Access-Control-Allow-Origin", "*")
            return meduses
        elif beach == "platjes_catalunya":
            beaches = beaches_catalunya(lang);
            response.set_header("Access-Control-Allow-Origin", "*")
            return beaches
        else:
            abort(404, "Beach %s is not found" % beach)

    jellyfishes = []
    jellyfishesHazard = jellyfishes_by_beach(settings.BEACHES[beach], lang)
    for jelly in jellyfishesHazard:
        aux_jelly = jellyfish_info(lang, jelly)
        aux_jelly["bloom_probability"] = bloom_probability(settings.BEACHES_TABLES[aux_jelly['scientific_name']],settings.BEACHES[beach])
        jellyfishes.append(aux_jelly)

    response.set_header("Access-Control-Allow-Origin", "*")
    return {'jellyfishes': jellyfishes}


if __name__ == "__main__":
    run(host='localhost', app=app, port=8080, debug=True, reloader=True)
