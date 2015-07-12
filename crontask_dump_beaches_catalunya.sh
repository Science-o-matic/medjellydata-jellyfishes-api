#!/bin/bash

LANG=ca_ES ~/.virtualenvs/medjellydata-jellyfishes-api/bin/python dump_beaches_catalunya.py > ~/www/medjellydata-jellyfishes-api/static/json/ca_ES/platjes_catalunya
LANG=es_ES ~/.virtualenvs/medjellydata-jellyfishes-api/bin/python dump_beaches_catalunya.py > ~/www/medjellydata-jellyfishes-api/static/json/es_ES/platjes_catalunya
LANG=en_EN ~/.virtualenvs/medjellydata-jellyfishes-api/bin/python dump_beaches_catalunya.py > ~/www/medjellydata-jellyfishes-api/static/json/en_EN/platjes_catalunya
LANG=de_DE ~/.virtualenvs/medjellydata-jellyfishes-api/bin/python dump_beaches_catalunya.py > ~/www/medjellydata-jellyfishes-api/static/json/de_DE/platjes_catalunya
LANG=fr_FR ~/.virtualenvs/medjellydata-jellyfishes-api/bin/python dump_beaches_catalunya.py > ~/www/medjellydata-jellyfishes-api/static/json/fr_FR/platjes_catalunya
LANG=it_IT ~/.virtualenvs/medjellydata-jellyfishes-api/bin/python dump_beaches_catalunya.py > ~/www/medjellydata-jellyfishes-api/static/json/it_IT/platjes_catalunya
LANG=ru_RU ~/.virtualenvs/medjellydata-jellyfishes-api/bin/python dump_beaches_catalunya.py > ~/www/medjellydata-jellyfishes-api/static/json/ru_RU/platjes_catalunya
