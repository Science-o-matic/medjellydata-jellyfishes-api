# -*- coding: utf-8 -*-
from settings import IMG_URL

JELLYFISHES = {
    1: {
        'scientific_name': "Pelagia noctiluca",
        'common_name': "Medusa luminescent",
        'photo': IMG_URL + "pelagia.png",
        'description': """
<p>Aquesta espècie és considerada una de les més abundants i importants al llarg de la costa catalana. És una espècie oceànica, per la qual cosa la seva presència en aigües costaneres depèn de les condicions ambientals i climatològiques. És molt freqüent la primavera i l’estiu, tot i que la seva presència es pot detectar durant tot l'any.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En aquest cas, l'espècie Pelagia noctiluca és considerada una espècie MOLT urticant, però a causa de que la seva abundància és de categoria 1 (<1 individu / 10 m2), el nivell de perillositat específic per aquest dia en aquesta platja és nivell 2 (Presència de Meduses AMB Perill).</p>
""",
            "VERY_HIGH_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En aquest cas, l'espècie Pelagia noctiluca és considerada una espècie MOLT urticant i degut a que la seva abundància és de categoria 2 (>1 individu / 10 m2), el nivell de perillositat específic per a aquest dia en aquesta platja és nivell 3 (Presència de Meduses d’ALT Perill).</p>
"""
            },
        },
    2: {
        'scientific_name': "Rhizostoma pulmo",
        'common_name': "Born blau",
        'photo': IMG_URL + "rhizostoma.png",
        'description': """
<p>És la medusa més gran de la costa Catalana (10-40 cm de diàmetre). És considerada una espècie costanera, present generalment a la superfície o propera a la superfície. És molt abundant al llarg de la costa Catalana. Les meduses petites es produeixen a la primavera i els adults de major grandària són més evidents a l'estiu i al començament de la tardor.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En aquest cas, l'espècie Rhizostoma pulmo és considerada una espècie URTICANT, però a causa que la seva abundància és de categoria 1 (<1 individu / 10 m2), el nivell de perillositat específic per a aquest dia en aquesta platja és de nivell 1 (Presència de Meduses SENSE Perill).</p>
""",
            "HIGH_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En aquest cas, l'espècie Rhizostoma pulmo és considerada una espècie URTICANT, i degut a que la seva abundància és de categoria 2 (>1 individu / 10 m2), el nivell de perillositat específic per a aquest dia en aquesta platja és nivell 2 (Presència de Meduses AMB Perill).</p>
"""
            }
        },
    3: {
        'scientific_name': "Aequorea forskalea",
        'common_name': "Medusa aequorea",
        'photo': IMG_URL + "aequorea.png",
        'description': """
<p>Durant els últims anys s'ha convertit en una espècie freqüent a la costa Catalana, i quan ocorre, ho fa en grans nombres. Aquesta espècie habita des d'aigües temperades a tropicals, en àrees costaneres i litorals, trobant-se fins i tot de forma ocasional en mar obert.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En el cas d’ Aequorea forskalea en ser una espècie LLEUGERAMENT urticant, el nivell de perillositat és 1 (Presència de meduses SENSE perill) independent de l'abundància en la qual estigui present a la platja, ja que la seva presència no representa cap perill per als banyistes.</p>
""",
            },
        },
    4: {
        'scientific_name': "Cotylorhiza tuberculata",
        'common_name': " Medusa ou ferrat",
        'photo': IMG_URL + "cotylorhiza.png",
        'description': """
<p>És una espècie endèmica del Mediterrani i és molt freqüent en la costa Catalana. És una espècie costanera, amb preferència d'aigües més càlides. Els adults són més abundants a la fi de l'estiu i principis de la tardor.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En el cas de Cotylorhiza tuberculata en ser una espècie LLEUGERAMENT urticant, el nivell de perillositat és 1 (Presència de meduses SENSE perill) independentment de l'abundància en la qual estigui present a la platja, ja que la seva presència no representa cap perill per als banyistes.</p>
""",
            },
        },
    5: {
        'scientific_name': "Velella velella",
        'common_name': "Barquetes de Sant Pere",
        'photo': IMG_URL + "velella.png",
        'description': """
<p>Al llarg de la costa Catalana, com en tot el Mediterrani, és una espècie molt freqüent especialment durant la primavera. Viu a l’interfase d’aigua/aire amb el flotador sobre l'aigua. Pot estar present en grans eixams aconseguint fins i tot diversos quilòmetres. Com el seu moviment depèn totalment dels corrents i dels vents de superfície, poden ser portades a la línia de costa i trobar-se encallades a les platges.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En el cas de Velella velella en ser una espècie LLEUGERAMENT urticant, el nivell de perillositat és 1 (Presència de meduses SENSE perill) independent de l'abundància en la qual estigui present a la platja, ja que la seva presència no representa cap perill per als banyistes.</p>
""",
            },
        },
    6: {
        'scientific_name': "Aurelia aurita",
        'common_name': "Medusa lluna",
        'photo': IMG_URL + "aurelia.png",
        'description': """
<p>La freqüència d'aquesta espècie al llarg de la costa Catalana ha disminuït en els últims anys i actualment és considerada una espècie de baixa freqüència. Quan està present, pot ser observada al final de la primavera. És una espècie costanera i es pot trobar fins i tot en estuaris i ports.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En el cas d’ Aurelia aurita en ser una espècie LLEUGERAMENT urticant, el nivell de perillositat és 1 (Presència de meduses SENSE perill) independent de l'abundància en la qual estigui present a la platja, ja que la seva presència no representa cap perill per als banyistes.</p>
""",
            },
        },
    7: {
        'scientific_name': "Chrysaora hysoscella",
        'common_name': "Born radiat",
        'photo': IMG_URL + "chrysaora.png",
        'description': """
<p>És una espècie pelàgica relativament gran (diàmetre fins a 30 cm). Malgrat que pot ser bastant abundant en alguna àrees del Mediterrani espanyol, a la costa Catalana és considerada una espècie poc freqüent i comunament present a la primavera.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En aquest cas, l'espècie Chrysaora hysoscella és considerada una espècie MOLT urticant, però a causa de que la seva abundància és de categoria 1 (<1 individu / 10 m2), el nivell de perillositat específic per a aquest dia en aquesta platja és nivell 2 (Presència de Meduses AMB Perill).</p>
""",
            "VERY_HIGH_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En aquest cas, l'espècie Chrysaora hysoscella és considerada una espècie MOLT urticant, i degut a que la seva abundància és de categoria 2 (>1 individu / 10 m2), el nivell de perillositat específic per a aquest dia en aquesta platja és nivell 3 (Presència de Meduses d’ALT Perill).</p>
"""
            },
        },
    8: {
        'scientific_name': "Porpita porpita",
        'common_name': "Botó blau",
        'photo': IMG_URL + "porpita.png",
        'description': """
<p>Aquesta espècie viu sobre la superfície de l'oceà però a vegades són arrossegades fins a la riba,on poden ser vistes ocasionalment en milers. Al llarg de la costa Catalana aquesta espècie és considerada rara.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En el cas de Porpita porpita en ser una espècie LLEUGERAMENT urticant, el nivell de perillositat és 1 (Presència de meduses SENSE perill) independent de l'abundància en la qual estigui present a la platja, ja que la seva presència no representa cap perill per als banyistes.</p>
""",
            },
        },
    9: {
        'scientific_name': "Carybdea marsupialis",
        'common_name': "Cubomedusa",
        'photo': IMG_URL + "carybdea.png",
        'description': """
<p>Malgrat que C. marsupialis és una cubomedusa, el seu verí no és letal.</p>
<p> L'ambient preferit d'aquesta espècie sembla ser el substrat sorrenc, i es localitza sobre el fons durant el dia desplaçant-se a la superfície durant la nit. Aquesta espècie està present en alta abundància en algunes àrees de la costa Espanyola Mediterrània, però al llarg de la costa Catalana és considerada molt rara, malgrat que la seva presència podria estar subestimada.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En aquest cas, l'espècie Carybdea marsupialis és considerada una espècie MOLT urticant, però degut a que la seva abundància és de categoria 1 (<1 individu / 10 m2), el nivell de perillositat específic per a aquest dia en aquesta platja és nivell 2 (Presència de Meduses AMB Perill).</p>
""",
            "VERY_HIGH_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En aquest cas, l'espècie Carybdea marsupialis és considerada una espècie MOLT urticant, degut a que la seva abundància és de categoria 2 (>1 individu / 10 m2), el nivell de perillositat específic per a aquest dia en aquesta platja és nivell 3 (Presència de Meduses ALT Perill).</p>
""",
            },
        },
    10: {
        'scientific_name': "Physalia physalis",
        'common_name': "Caravel·la portuguesa",
        'photo': IMG_URL + "physalia.png",
        'description': """
<p>És una animal marí pelàgic que sura per la superfície del mar i és arrossegada pels vents i corrents. És més comú a mar obert, però els corrents i vents poden portar-les a aigües poc profundes i costaneres. En el Mediterrani no es troba de forma freqüent i al llarg de la costa Catalana és considerada molt rara, malgrat que s'han reportat algunes observacions aïllades en els últims anys.</p>
""",
        'risk_description': {
            "VERY_HIGH_WARNING": """
<p>El nivell perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En aquest cas, l'espècie Physalia physalis és considerada una espècie MOLT urticant, per la qual cosa el nivell de perillositat a la platja on es trobi és nivell 3 (Presència de Meduses d’ALT Perill) independent de l'abundància. La presència de tan sols un individu de P. physalis a nivell de platja es considera una situació de perill per als banyistes.</p>
""",
            },
        },
    11: {
        'scientific_name': "Olindias phosphorica",
        'common_name': "Medusa creu",
        'photo': IMG_URL + "olindias.png",
        'description': """
<p>La presència d'aquesta espècie al llarg de la costa Catalana és esporàdica. Mai s'observen bancs extensos però pot ser molt abundant localment. En anys recents, està sent molt abundant en la costa de Tunísia al Mediterrani, causant problemes per a la indústria del turisme.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En aquest cas, l'espècie Olindias phosphorica és considerada una espècie MOLT urticant, però degut a que la seva abundància és de categoria 1 (<1 individu / 10 m2), el nivell de perillositat específic per a aquest dia en aquesta platja és nivell 2 (Presència de Meduses AMB Perill).</p>
""",
            "VERY_HIGH_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En aquest cas, l'espècie Olindias phosphorica és considerada una espècie MOLT urticant, i degut a que la seva abundància és de categoria 2 (>1 individu / 10 m2), el nivell de perillositat específic per a aquest dia en aquesta platja és nivell 3 (Presència de Meduses d’ALT Perill).</p>
"""
            },
        },
    12: {
        'scientific_name': "Mnemiopsis leidyi",
        'common_name': "Medusa bombeta",
        'photo': IMG_URL + "leidyi.png",
        'description': """
<p>Aquesta espècie no és un cnidari sinó un ctenòfor, per la qual cosa no té cnidocists (cèl·lules urticants) i per tant és inofensiu per als humans, però molt nociu per als ecosistemes marins envaïts. És una espècie invasora que va ser reportada per primera vegada en la costa Catalana l'any 2009.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En el cas de Mnemiopsis leidyi en ser una espècie NO urticant, el nivell de perillositat és 1 (Presència de meduses SENSE perill) independent de l'abundància en la qual estigui present a la platja, ja que la seva presència no representa cap perill per als banyistes.</p>
""",
            },
        },
    13: {
        'scientific_name': "Phyllorhiza punctata",
        'common_name': "Medusa de pigues blanques",
        'photo': IMG_URL + "punctata.png",
        'description': """
<p>Aquesta espècie és una medusa costanera i d'estuaris, la distribució nativa dels quals inclou Austràlia i gran part de l'Indo-Pacífic. És una espècie invasora, i va ser reportada per primera vegada l'any 2010 al sud de la costa Catalana.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>El nivell de perillositat de la presència de meduses a les platges s'obté a través d'un índex que considera la capacitat urticant pròpia de l'espècie i la seva abundància a les aigües de bany. En el cas de Phyllorhiza punctata en ser una espècie LLEUGERAMENT urticant, el nivell de perillositat és 1 (Presència de meduses SENSE perill) independent de l'abundància en la qual estigui present a la platja, ja que la seva presència no representa cap perill per als banyistes.</p>
""",
            },
        },
    }
