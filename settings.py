# -*- coding: utf-8 -*-
MEDJELLY_API_BASE_URL = 'https://app.bahiasoftware.es/MEDUSAS/ws/'

LANGUAGES = ('es_ES',)

# Beaches paths and its correspoding MedJelly API id
BEACHES = {
    "portbou/portbou": 40,
    "colera/goixa": 41,
    "colera/garbet": 42,
    "lanca/grifeu": 43,
    "llanca/port": 44,
    "llanca/farella": 45,
    "llanca/caullop":46,
    "portselva/portvall": 47,
    "portselva/portselva": 48,
    "portselva/pas": 49,
    "portselva/tamariua": 50,
    "cadaques/ros": 51,
    "cadaques/grancadaques": 52,
    "cadaques/llanegran": 53,
    "roses/montjoi": 54,
    "roses/almadrava": 55,
    "roses/canyellespetites": 56,
    "roses/palangrers": 57,
    "roses/punta": 58,
    "roses/nova": 0,
    "roses/roses": 59,
    "roses/salatar": 0,
    "roses/santamargarida": 60,
    "castelloempuries/rubina": 61,
    "castelloempuries/empuriabrava": 62,
    "castelloempuries/muga": 0,
    "castelloempuries/cangomes": 63,
    "santperepescador/gola": 64,
    "santperepescador/canmartinet": 0,
    "santperepescador/cannera": 0,
    "santperepescador/cansopa": 0,
    "santperepescador/calcristia": 0,
    "santperepescador/cortalvila": 0,
    "santperepescador/cortaldevesa": 0,
    "santperepescador/riuet": 0,
    # santerperepescador/santperescador: 65
    "escala/mollgrec": 66,
    "escala/muscleres": 67,
    "escala/portitxol": 0,
    "escala/rec": 68,
    "escala/platja": 69,
    "escala/riells": 70,
    "torroellamontgri/montgo": 71,
    "torroellamontgri/estartit": 72,
    "torroellamontgri/gola": 73,
    "pals/grau": 74,
    "pals/granpals": 75,
    "begur/raco": 76,
    "begur/illaroja": 77,
    "begur/riera": 78,
    "begur/tuna": 79,
    "begur/fonda": 80,
    "begur/aiguablava": 81,
    "palafrugell/tamariu": 82,
    "palafrugell/llafranc": 83,
    "palafrugell/canadell": 84,
    "palafrugell/portbo": 85,
    "palafrugell/portpelegri": 0,
    "palafrugell/golfet": 86,
    "montras/crit": 87,
    "palamos/estreta": 88,
    "palamos/castell": 89,
    "palamos/fosca": 90,
    "palamos/margarida": 91,
    "palamos/morrovedell": 0,
    "palamos/granpalamos": 92,
    "calonge/monestri": 93,
    "calonge/santantoni": 94,
    "calonge/torrevalentina": 95,
    "calonge/cristus": 96,
    "calonge/torretes": 96,
    "castellplatjaaro/rovira": 97,
    "castellplatjaaro/aro": 98,
    "castellplatjaaro/conca": 99,
    "santfeliuguixols/santpol": 100,
    "santfeliuguixols/santfeliu": 101,
    "santfeliuguixols/canyerets": 102,
    "santacristinaaro/senyorramon": 103,
    "tossamar/salionc": 104,
    "tossamar/giverola": 105,
    "tossamar/marmenuda": 106,
    "tossamar/tossa": 107,
    "tossamar/codolar": 108,
    "tossamar/llorell": 109,
    "lloretmar/canyelles": 110,
    "lloretmar/lloret": 111,
    "lloretmar/fenals": 112,
    "lloretmar/boadella": 113,
    "lloretmar/santacristina": 114,
    "blanes/santfrancesc": 115,
    "blanes/blanes": 116,
    "blanes/sabanell": 117,
    "malgratmar/tordera": 118,
    "malgratmar/conca": 0,
    "malgratmar/malgratcentre": 119,
    "malgratmar/astillero": 120,
    #"santasusanna/santasusanna": 121,
    "santasusanna/llevant": 0,
    "santasusanna/dunes": 0,
    "pinedamar/pins": 122,
    "pinedamar/pescadors": 0,
    "pinedamar/riera": 0,
    "pinedamar/poblenou": 123,
    "calella/grancalella": 124,
    "calella/garbi": 125,
    "calella/roques": 126,
    "santpolmar/morer": 127,
    "santpolmar/escaletesplatjola": 0,     # es la misma que morer?
    "santpolmar/santpol": 128,
    "santpolmar/grau": 129,
    "santpolmar/farell": 130,
    "santpolmar/moli": 131,
    "canetmar/canet": 132,
    "canetmar/cavaio": 133,
    "arenysmar/cavaio": 134,
    "arenysmar/picordia": 135,
    "arenysmar/roqueslluc": 136,
    "arenysmar/musclera": 137,
    "caldesestrac/riera": 138,
    "caldesestrac/tresmicos": 139,
    "santvicencmontalt/santvicencmontalt": 140,
    "santandreullavaneres/barques": 0,
    "santandreullavaneres/estacio": 0,
    # "santandreullavaneres/santandreullavaneres": 141,
    "mataro/santsimo": 142,
    "mataro/callao": 143,
    "mataro/varador": 144,
    "mataro/ponent": 0,
    #     "cabreramar/cabreramar": 145,
    "cabreramar/moli": 0,
    "cabreramar/vinyals": 0,
    # "vilassarmar/vilassarmar": 146
    "vilassarmar/almadrava": 0,
    "vilassarmar/astillero": 0,
    "vilassarmar/ponent": 0,
    "premiamar/llevant": 0,
    "premiamar/bellamar": 0,
    "premiamar/plaos": 147,
    "premiamar/descarrega": 0,
    "premiamar/ponent": 0,
    "masnou/ocata": 148,
    "masnou/masnou": 149,
    "montgat/plamontgat": 12,
    "montgat/santjoan": 11,
    "montgat/moreres": 0,
    "badalona/barcamaria": 21,
    "badalona/cristall": 20,
    "badalona/pontbotifarreta": 19,
    "badalona/pescadors": 18,
    "badalona/patins": 17,
    "badalona/estacio": 16,
    "badalona/pontpetroli": 15,
    "badalona/coco": 23,
    "badalona/mora": 22,
    "santadriabesos/parclitoral": 25,
    "santadriabesos/parcpau": 0,
    "barcelona/zonabanysforum": 24,
    "barcelona/llevant": 9,
    "barcelona/novamarbella": 8,
    "barcelona/marbella": 7,
    "barcelona/bogatell": 6,
    "barcelona/novaicaria": 5,
    "barcelona/somorrostro": 4,
    "barcelona/barceloneta": 3,
    "barcelona/santmiquel": 2,
    "barcelona/santsebastia": 1,
    "pratllobregat/prat": 27,
    "viladecans/viladecans": 151,
    "gava/gava": 152,
    "castelldefels/pineda": 39,
    "castelldefels/lluminetes": 38,
    "castelldefels/baixador": 37,
    "sitges/botigues": 154,
    "sitges/garraf": 155,
    "sitges/aiguadolc": 156,
    "sitges/balmins": 157,
    "sitges/santsebastia": 0,
    "sitges/fragata": 0,
    "sitges/ribera": 158,
    "sitges/bassarodona": 0,
    "sitges/estanyol": 159,
    "sitges/rieraxica": 0,
    "sitges/barra": 160,
    "sitges/terramar": 161,
    "sitges/anquines": 0,
    "vilanovageltru/farsantcristofol": 162,
    "vilanovageltru/ribesroges": 163,
    "vilanovageltru/adarro": 164,
    "vilanovageltru/santgervasi": 165,
    "vilanovageltru/llarga": 0,
    "vilanovageltru/ibersol": 166,
    "cubelles/llarga": 167,
    "cubelles/motasantpere": 168,
    "cubelles/salines": 0,
    "cubelles/gavines": 0,
    "cunit/cunit": 169,
    "calafell/segurcalafell": 170,
    "calafell/estanymasmel": 171,
    "calafell/calafell": 172,
    "vendrell/santsalvador": 173,
    "vendrell/comaruga": 174,
    "vendrell/francas": 175,
    "rodabera/costadaurada": 176,
    "rodabera/pelliseta": 0,
    "rodabera/puntaguineu": 177,
    "rodabera/llarga": 178,
    "creixell/creixell": 179,
    "torredembarra/muntanyans": 180,
    "torredembarra/barrimaritim": 181,
    "torredembarra/paella": 182,
    "torredembarra/canyadell": 0,
    "altafulla/altafulla": 183,
    "altafulla/tamarit": 0,
    "tarragona/tamarit": 184,
    "tarragona/jovera": 0,
    "tarragona/mora": 185,
    "tarragona/rocaplana": 0,
    "tarragona/fonda": 0,
    "tarragona/llarga3": 186,
    "tarragona/llarga2": 186,
    "tarragona/llarga1": 186,
    "tarragona/capellans": 0,
    "tarragona/savinosa": 187,
    "tarragona/arrabassada": 188,
    "tarragona/miracle": 189,
    "tarragona/comandancia": 0,
    "vilaseca/pineda": 191,
    "vilaseca/raco": 192,
    "salou/crancs": 193,
    "salou/font": 194,
    "salou/llarga": 195,
    "salou/capellans": 196,
    "salou/llevant": 197,
    "salou/ponent": 198,
    "cambrils/capsantpere": 199,
    "cambrils/vilafortuny": 200,
    "cambrils/esquirol": 201,
    "cambrils/cavet": 202,
    "cambrils/prat fores": 203,
    "cambrils/riera": 0,
    "cambrils/hortasantamaria": 204,
    "cambrils/llosa": 205,
    "cambrils/dorado": 0, # error? dorada?
    "cambrils/ardiaca": 206,
    "cambrils/dorada": 207,
    "montroigcamp/pixerota": 208,
    "montroigcamp/porquerola": 209,
    "montroigcamp/casalladres": 210,
    "montroigcamp/vienesos": 211,
    "montroigcamp/cristall": 212,
    "vandellost/puntariu": 213,
    "vandellos/arenal": 214,
    "vandellos/torn": 215,
    "vandellos/almadrava": 216,
    "ametllamar/calafato": 217,
    "ametllamar/santjordialfama": 218,
    "ametllamar/forn": 219,
    "ametllamar/pixavaques": 220,
    "ametllamar/alguer": 222,
    "ametllamar/estany": 221,
    "perello/aliga": 223,
    "perello/santallucia": 224,
    "perello/buena": 225,
    "ampolla/caproig": 226,
    "ampolla/avellaners": 227,
    "ampolla/arenal": 228,
    "deltebre/marquesa": 229,
    "deltebre/bassa d'arena": 0,
    "deltebre/riumar": 231,
    "santjaumeenveja/migjorn": 232,
    "santjaumeenveja/serrallo": 233,
    "amposta/eucaliptus": 235,
    "santcarlesrapita/trabucador": 236,
    "santcarlesrapita/aluet": 0,
    "santcarlesrapita/parcgarbi": 238,
    "santcarlesrapita/hortets": 0,
    "santcarlesrapita/capri": 0,
    "santcarlesrapita/aiguassera": 0,
    "santcarlesrapita/senieta": 0,
    "santcarlesrapita/far": 0,
    "santcarlesrapita/delicies": 239,
    "santcarlesrapita/suis": 0,
    "alcanar/martinenca": 240,
    "alcanar/maricel": 241,
    "alcanar/cases d'alcanar": 242,
    "alcanar/marjal": 243
    }

NO_RISK = 1
RISK = 2
HIGH_RISK = 3

RISK_LEVELS = {
    NO_RISK: {
        'es_ES': 'Presencia de Medusas SIN peligro',
        },
    RISK: {
        'es_ES': 'Presencia de Medusas CON peligro',
        },
    HIGH_RISK: {
        'es_ES': 'Presencia de Medusas ALTO peligro'
    },
}

SOURCE_NOTES = {
    'es_ES': """
<p>Nota: Toda la información ha sido validada por el Instituto de Ciencias del Mar –CSIC de Barcelona a través de la colaboración entre la Agencia Catalana del Agua y el Proyecto Europeo MED-JELLYRISK.</p>
<p>Para más información sobre MEDUSAS visitar la web del proyecto www.jellyrisk.eu o descarga la App iMedjelly (Descarga gratuita para iPhone y Android).</p>
"""
}



# Jellyfishes by MedJelly API id
JELLYFISHES = {
    1: {'name': 'Pelagia noctiluca',
        # Danger level by specimen quantity
        'danger_level': {
            1: 4,
            2: 5,
            3: 5
            }
        },
    2: {'name': 'Rhizostoma pulmo',
        'danger_level': {
            1: 3,
            2: 4,
            3: 4
            }
        },
    3: {'name': 'Aequorea forskalea',
        'danger_level': {
            1: 3,
            2: 3,
            3: 3
            }
        },
    4: {'name': 'Cotylorhiza tuberculata',
        'danger_level': {
            1: 3,
            2: 3,
            3: 3
            },
        },
    5: {'name': 'Velella velella',
        'danger_level': {
            1: 3,
            2: 3,
            3: 3
            },
        },
    6: {'name': 'Aurelia aurita',
        'danger_level': {
            1: 3,
            2: 3,
            3: 3
            },
        },
    7: {'name': 'Chrysaora hysoscella',
        'danger_level': {
            1: 4,
            2: 5,
            3: 5
            },
        },
    8: {'name': 'Porpita porpita',
        'danger_level': {
            1: 3,
            2: 3,
            3: 3
            },
        },
    9: {'name': 'Carybdea marsupialis',
        'danger_level': {
            1: 4,
            2: 5,
            3: 5
            },
        },
    10: {'name': 'Physalia physalis',
        'danger_level': {
            1: 5,
            2: 5,
            3: 5
            },
        },
    11: {'name': 'Olindias phosphorica',
        'danger_level': {
            1: 4,
            2: 5,
            3: 5
            },
        },
    12: {'name': 'Mnemiopsis leidyi',
        'danger_level': {
            1: 3,
            2: 3,
            3: 3
            },
        },
    13: {'name': 'Phyllorhiza punctata',
        'danger_level': {
            1: 3,
            2: 3,
            3: 3
            },
        },
    14: {'name': 'Cassiopea andromeda',
        'danger_level': {},
        },
    15: {'name': 'Salpa',
        'danger_level': {},
         }
    }
