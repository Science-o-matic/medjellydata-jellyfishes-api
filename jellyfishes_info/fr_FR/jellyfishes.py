# -*- coding: utf-8 -*-
from settings import IMG_URL


JELLYFISHES = {
    1: {
        'scientific_name': "Pelagia noctiluca",
        'common_name': "Méduse pélagique",
        'photo': IMG_URL + "pelagia.png",
        'description': """
<p>Cette espèce est considérée comme l’une des plus abondantes et importantes le long de la côte catalane. Comme il s’agit d’une espèce océanique, sa présence dans les eaux côtières dépend des conditions environnementales et climatologiques. Cette méduse est très fréquente au printemps et en été, bien que sa présence puisse être détectée pendant toute l’année.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans ce cas, l’espèce Pelagia noctiluca est considérée comme TRÈS urticante, mais du fait que son abondance correspond à la catégorie %(abundance)i %(abundance_ratio)s, la dangerosité spécifique pour cette journée sur cette plage est de niveau 2 (Présence de méduses représentant un DANGER).</p>
""",
            "VERY_HIGH_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans ce cas, étant donné que l’espèce Pelagia noctiluca est considérée comme TRÈS urticante et que son abondance correspond à la catégorie %(abundance)i %(abundance_ratio)s, la dangerosité spécifique pour cette journée sur cette plage est de niveau 3 (Présence de méduses représentant un DANGER IMPORTANT).</p>
"""
            },
        },
    2: {
        'scientific_name': "Rhizostoma pulmo",
        'common_name': "Rhizostome ou poumon de mer",
        'photo': IMG_URL + "rhizostoma.png",
        'description': """
<p>Il s’agit de la plus grande méduse de la côte catalane (10-40 cm de diamètre). Considérée comme une espèce côtière, elle est généralement présente en surface ou à proximité de la surface et s’avère très abondante le long de la côte catalane. Les jeunes méduses s’observent au printemps, tandis que les adultes, de plus grande taille, sont plus fréquents en été et au début de l’automne.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans ce cas, l’espèce Rhizostoma pulmo est considérée comme URTICANTE, mais du fait que son abondance correspond à la catégorie %(abundance)i %(abundance_ratio)s, la dangerosité spécifique pour cette journée sur cette plage est de niveau 1 (Présence de méduses ne représentant PAS DE DANGER).</p>
""",
            "HIGH_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans ce cas, étant donné que l’espèce Rhizostoma pulmo est considérée comme TRÈS urticante et que son abondance correspond à la catégorie %(abundance)i %(abundance_ratio)s, la dangerosité spécifique pour cette journée sur cette plage est de niveau 2 (Présence de méduses représentant un DANGER).</p>
"""
            }
        },
    3: {
        'scientific_name': "Aequorea forskalea",
        'common_name': "Équorée",
        'photo': IMG_URL + "aequorea.png",
        'description': """
<p>Au cours des dernières, l’équorée est devenue une espèce fréquente sur la côte catalane. En cas de présence, on la trouve en grand nombre. Son habitat s’étend depuis les eaux tempérées jusqu’aux eaux tropicales. Elle vit surtout dans les zones côtières et littorales, mais se rencontre aussi parfois en haute mer.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans le cas d’Aequorea forskalea, une espèce LÉGÈREMENT urticante, le niveau de dangerosité vaut 1 (Présence de méduses ne représentant PAS DE DANGER) indépendamment de l’abondance de cette espèce sur la plage, car sa présence ne présente aucun danger pour les baigneurs.</p>
""",
            },
        },
    4: {
        'scientific_name': "Cotylorhiza tuberculata",
        'common_name': "Méduse œuf au plat",
        'photo': IMG_URL + "cotylorhiza.png",
        'description': """
<p>Très fréquente sur la côte catalane, la méduse œuf au plat est une espèce endémique de la Méditerranée. Il s’agit d’une espèce côtière qui affectionne les eaux plus chaudes. Les adultes sont plus abondants à la fin de l’été ou au début de l’automne.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans le cas de Cotylorhiza tuberculata, une espèce LÉGÈREMENT urticante, le niveau de dangerosité vaut 1 (Présence de méduses ne représentant PAS DE DANGER) indépendamment de l’abondance de cette espèce sur la plage, car sa présence ne présente aucun danger pour les baigneurs.</p>
""",
            },
        },
    5: {
        'scientific_name': "Velella velella",
        'common_name': "Vélelle",
        'photo': IMG_URL + "velella.png",
        'description': """
<p>Le long de la côte catalane, comme dans toute la Méditerranée, la vélelle est une espèce très fréquente, surtout au printemps. Elle vit à l’interface entre l’eau et l’air avec son flotteur sur l’eau. On la trouve parfois en grandes colonies de jusqu’à plusieurs kilomètres. Comme leur mouvement dépend totalement des courants et des vents de surface, les vélelles peuvent être amenées sur la ligne de côte et échouer sur les plages.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans le cas de Velella velella, une espèce LÉGÈREMENT urticante, le niveau de dangerosité vaut 1 (Présence de méduses ne représentant PAS DE DANGER) indépendamment de l’abondance de cette espèce sur la plage, car sa présence ne présente aucun danger pour les baigneurs.</p>
""",
            },
        },
    6: {
        'scientific_name': "Aurelia aurita",
        'common_name': "Aurélie ou méduse commune",
        'photo': IMG_URL + "aurelia.png",
        'description': """
<p>Le long de la côte catalane, la fréquence de la méduse aurélie a diminué au cours des dernières années et cette espèce est considérée aujourd’hui comme peu fréquente. Quand elle est présente, on l’observe à la fin du printemps. C’est une espèce côtière qui peut même se trouver dans les estuaires et les ports.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans le cas d’Aurelia aurita, une espèce LÉGÈREMENT urticante, le niveau de dangerosité vaut 1 (Présence de méduses ne représentant PAS DE DANGER) indépendamment de l’abondance de cette espèce sur la plage, car sa présence ne présente aucun danger pour les baigneurs.</p>
""",
            },
        },
    7: {
        'scientific_name': "Chrysaora hysoscella",
        'common_name': "Méduse rayonnée",
        'photo': IMG_URL + "chrysaora.png",
        'description': """
<p>Il s’agit d’une espèce pélagique relativement grande (diamètre de jusqu’à 30 cm). Bien qu’elle puisse être assez abondante dans certaines zones de la Méditerranée espagnole, on la considère comme une espèce peu fréquente sur la côte catalane et communément présente au printemps.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans ce cas, l’espèce Chrysaora hysoscella est considérée comme TRÈS urticante, mais du fait que son abondance correspond à la catégorie %(abundance)i %(abundance_ratio)s, la dangerosité spécifique pour cette journée sur cette plage est de niveau 2 (Présence de méduses représentant un DANGER).</p>
""",
            "VERY_HIGH_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans ce cas, étant donné que l’espèce Chrysaora hysoscella est considérée comme TRÈS urticante et que son abondance correspond à la catégorie %(abundance)i %(abundance_ratio)s, la dangerosité spécifique pour cette journée sur cette plage est de niveau 3 (Présence de méduses représentant un DANGER IMPORTANT).</p>
"""
            },
        },
    8: {
        'scientific_name': "Porpita porpita",
        'common_name': "Porpite",
        'photo': IMG_URL + "porpita.png",
        'description': """
<p>Bien que vivant à la surface de l’océan, les porpites sont parfois entraînées jusqu’au rivage, où l’on peut les observer par milliers à certaines occasions. Le long de la côte catalane, cette espèce est considérée comme rare.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans le cas de Porpita porpita, une espèce LÉGÈREMENT urticante, le niveau de dangerosité vaut 1 (Présence de méduses ne représentant PAS DE DANGER) indépendamment de l’abondance de cette espèce sur la plage, car sa présence ne présente aucun danger pour les baigneurs.</p>
""",
            },
        },
    9: {
        'scientific_name': "Carybdea marsupialis",
        'common_name': "Carybdée marsupiale",
        'photo': IMG_URL + "carybdea.png",
        'description': """
<p>Bien que la Carybdea marsupialis soit une cuboméduse, son venin n’est pas mortel. Son milieu préféré semble être le substrat sableux. Elle se trouve sur les fonds pendant la journée et se déplace vers la surface la nuit. Présente en grande abondance dans certaines zones de la côte espagnole méditerranéenne, cette espèce est cependant considérée comme très rare le long de la côte catalane. Toutefois, sa présence pourrait être sous-estimée.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans ce cas, étant donné que l’espèce Carybdea marsupialis est considérée comme TRÈS urticante et que son abondance correspond à la catégorie %(abundance)i %(abundance_ratio)s, la dangerosité spécifique pour cette journée sur cette plage est de niveau 2 (Présence de méduses représentant un DANGER).</p>
""",
            "VERY_HIGH_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans ce cas, étant donné que l’espèce Carybdea marsupialis est considérée comme TRÈS urticante et que son abondance correspond à la catégorie %(abundance)i %(abundance_ratio)s, la dangerosité spécifique pour cette journée sur cette plage est de niveau 3 (Présence de méduses représentant un DANGER IMPORTANT).</p>
""",
            },
        },
    10: {
        'scientific_name': "Physalia physalis",
        'common_name': "Galère portugaise",
        'photo': IMG_URL + "physalia.png",
        'description': """
<p>Il s’agit d’un animal marin pélagique qui flotte à la surface de la mer et est entraîné par les vents et les courants. Lesdites galères portugaises sont plus communes en haute mer, mais les courants et les vents peuvent les amener dans les eaux peu profondes et côtières. Cette espèce ne se trouve pas fréquemment en Méditerranée et est considérée comme très rare le long de la côte catalane, bien que quelques observations isolées aient été rapportées au cours des dernières années.</p>
""",
        'risk_description': {
            "VERY_HIGH_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans ce cas, l’espèce Physalia physalis étant considérée comme TRÈS urticante, la dangerosité est de niveau 3 (Présence de méduses représentant un DANGER IMPORTANT) sur la plage où elle se trouve, et ce indépendamment de son abondance. La présence d’un seul spécimen de Physalia physalis sur la plage est considérée comme une situation de danger pour les baigneurs.</p>
""",
            },
        },
    11: {
        'scientific_name': "Olindias phosphorica",
        'common_name': "Olindias",
        'photo': IMG_URL + "olindias.png",
        'description': """
<p>La présence de cette espèce le long de la côte catalane est sporadique. On n’observe jamais de bancs étendus, mais cette espèce peut être très abondante localement. Au cours des dernières années, elle a été très abondante sur la côte méditerranéenne tunisienne, ce qui a causé des problèmes dans l’industrie du tourisme. </p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans ce cas, étant donné que l’espèce Olindias phosphorica est considérée comme TRÈS urticante et que son abondance correspond à la catégorie %(abundance)i %(abundance_ratio)s, la dangerosité spécifique pour cette journée sur cette plage est de niveau 2 (Présence de méduses représentant un DANGER).</p>
""",
            "VERY_HIGH_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans ce cas, étant donné que l’espèce Olindias phosphorica est considérée comme TRÈS urticante et que son abondance correspond à la catégorie %(abundance)i %(abundance_ratio)s, la dangerosité spécifique pour cette journée sur cette plage est de niveau 3 (Présence de méduses représentant un DANGER IMPORTANT).</p>
"""
            },
        },
    12: {
        'scientific_name': "Mnemiopsis leidyi",
        'common_name': "Mnéiopsis ou méduse américaine",
        'photo': IMG_URL + "leidyi.png",
        'description': """
<p>N’étant pas un cnidaire mais bien un cténophore, cette espèce n’a pas de cnidocystes (cellules urticantes) et s’avère donc inoffensive pour l’homme. Néanmoins, elle est très nocive pour les écosystèmes marins envahis. Il s’agit d’une espèce envahissante qui a été signalée pour la première fois sur la côte catalane en 2009</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans le cas de Mnemiopsis leidyi, une espèce NON urticante, le niveau de dangerosité vaut 1 (Présence de méduses ne représentant PAS DE DANGER) indépendamment de l’abondance de cette espèce sur la plage, car sa présence ne présente aucun danger pour les baigneurs.</p>
""",
            },
        },
    13: {
        'scientific_name': "Phyllorhiza punctata",
        'common_name': "Méduse constellée",
        'photo': IMG_URL + "punctata.png",
        'description': """
<p>Cette espèce vit sur les côtes et dans les estuaires. Son aire de répartition naturelle englobe l’Australie et une grande partie de l’Indo-Pacifique. Il s’agit d’une espèce envahissante qui a été signalée pour la première fois en 2010 au sud de la côte catalane.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Le niveau de dangerosité de la présence de méduses sur les plages s’obtient à travers un indice basé sur le pouvoir urticant et l’abondance de l’espèce dans les eaux de baignade. Dans le cas de Phyllorhiza punctata, une espèce LÉGÈREMENT urticante, le niveau de dangerosité vaut 1 (Présence de méduses ne représentant PAS DE DANGER) indépendamment de l’abondance de cette espèce sur la plage, car sa présence ne présente aucun danger pour les baigneurs.</p>
""",
            },
        },
    }
