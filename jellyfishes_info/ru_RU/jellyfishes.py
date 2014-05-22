# -*- coding: utf-8 -*-
from settings import IMG_URL

JELLYFISHES = {
    1: {
        'scientific_name': "Pelagia noctiluca",
        'common_name': "Пелагия ночесветка",
        'photo': IMG_URL + "pelagia.png",
        'description': """
<p>Данный вид считается одним из самых важных и распространенных вдоль побережья Каталонии. Это океанический вид, поэтому его присутствие в прибрежных водах зависит от экологических и климатических условий. Эти медузы очень часто встречаются весной и летом, хотя их можно наблюдать в течение всего года.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В данном случае вид Pelagia noctiluca считается ОЧЕНЬ жгучим видом, но поскольку по своей распространенности он относится к категории 1 (<1 особь/10 м2), то уровень опасности в этот день на данном пляже считается равным 2 (Встречаются ОПАСНЫЕ медузы).</p>
""",
            "VERY_HIGH_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В данном случае вид Pelagia noctiluca считается ОЧЕНЬ жгучим видом, и поскольку по своей распространенности он относится к категории 2 (>1 особь/10 м2), то уровень опасности в этот день на данном пляже считается равным 3 (Встречаются ОЧЕНЬ ОПАСНЫЕ медузы).</p>
"""
            },
        },
    2: {
        'scientific_name': "Rhizostoma pulmo",
        'common_name': "Медуза-корнерот",
        'photo': IMG_URL + "rhizostoma.png",
        'description': """
<p>Самая крупная медуза из встречающихся у побережья Каталонии (10–40 см в диаметре). Корнерот считается прибрежным видом, обычно держится у поверхности или в слоях воды, близких к поверхности. Этот вид очень распространен вдоль каталонского побережья. Мелкие медузы появляются весной, а взрослые, более крупные особи наблюдаются летом и в начале осени.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В данном случае вид Rhizostoma pulmo считается ЖГУЧИМ видом, но поскольку по своей распространенности он относится к категории 1 (<1 особь/10 м2), то уровень опасности в этот день на данном пляже считается равным 1 (Встречаются БЕЗОПАСНЫЕ медузы).</p>
""",
            "HIGH_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В данном случае вид Rhizostoma pulmo считается ЖГУЧИМ видом, и поскольку по своей распространенности он относится к категории 2 (>1 особь/10 м2), то уровень опасности в этот день на данном пляже считается равным 2 (Встречаются ОПАСНЫЕ медузы).</p>
"""
            }
        },
    3: {
        'scientific_name': "Aequorea forskalea",
        'common_name': "Медуза экворея",
        'photo': IMG_URL + "aequorea.png",
        'description': """
<p>В последние годы данный вид стал очень распространен у побережья Каталонии, и в тех местах, где он присутствует, наблюдается большое количество его особей. Эти медузы обитают в умеренных и тропических водах, в прибрежных и литоральных зонах, иногда могут встречаться и в открытом море.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В случае Aequorea forskalea вид считается СЛЕГКА жгучим видом, уровень опасности 1 (Встречаются БЕЗОПАСНЫЕ медузы), вне зависимости от количества медуз на пляже, поскольку их присутствие не представляет опасности для купающихся..</p>
""",
            },
        },
    4: {
        'scientific_name': "Cotylorhiza tuberculata",
        'common_name': "Обычное название: Средиземноморская медуза или медуза-«яичница»",
        'photo': IMG_URL + "cotylorhiza.png",
        'description': """
<p>Средиземноморский эндемичный вид, очень распространенный у побережья Каталонии. Эти прибрежные медузы предпочитают теплые воды. Взрослые особи чаще всего встречаются в конце лета и начале осени.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В случае Cotylorhiza tuberculata вид считается СЛЕГКА жгучим видом, уровень опасности 1 (Встречаются БЕЗОПАСНЫЕ медузы), вне зависимости от количества медуз на пляже, поскольку их присутствие не представляет опасности для купающихся.</p>
""",
            },
        },
    5: {
        'scientific_name': "Velella velella",
        'common_name': "Обычное название: Медуза-парусник",
        'photo': IMG_URL + "velella.png",
        'description': """
<p>Часто встречается вдоль побережья Каталонии и в целом в Средиземном море, особенно весной. Обитает на поверхности воды, держа «парус» над поверхностью воды. Эти животные могут жить в больших группах размером до нескольких километров. Поскольку их перемещение полностью зависит от течений и ветров у поверхности, то медузы-парусники могут быть вынесены на берег и лежать на пляжах.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В случае Velella velella вид считается СЛЕГКА жгучим видом, уровень опасности 1 (Встречаются БЕЗОПАСНЫЕ медузы), вне зависимости от количества медуз на пляже, поскольку их присутствие не представляет опасности для купающихся.</p>
""",
            },
        },
    6: {
        'scientific_name': "Aurelia aurita",
        'common_name': "Ушастая аурелия",
        'photo': IMG_URL + "aurelia.png",
        'description': """
<p>Распространенность данного вида вдоль побережья Каталонии снизилась в последние годы, и в настоящее время вид встречается довольно редко. Аурелия может наблюдаться в конце весны. Это прибрежные медузы, их можно увидеть даже в эстуариях и портах.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В случае Aurelia aurita вид считается СЛЕГКА жгучим видом, уровень опасности 1 (Встречаются БЕЗОПАСНЫЕ медузы), вне зависимости от количества медуз на пляже, поскольку их присутствие не представляет опасности для купающихся.</p>
""",
            },
        },
    7: {
        'scientific_name': "Chrysaora hysoscella",
        'common_name': "Медуза-компас",
        'photo': IMG_URL + "chrysaora.png",
        'description': """
<p>Это довольно крупный пелагический вид (диаметр до 30 см). Несмотря на то, что эти медузы очень распространены в некоторых зонах испанского Средиземноморья, у побережья Каталонии этот вид считается редким, обычно встречается весной.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В данном случае вид Chrysaora hysoscella считается ОЧЕНЬ жгучим видом, но поскольку по своей распространенности он относится к категории 1 (<1 особь/10 м2), то уровень опасности в этот день на данном пляже считается равным 2 (Встречаются ОПАСНЫЕ медузы).</p>
""",
            "VERY_HIGH_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В данном случае вид Chrysaora hysoscella считается ОЧЕНЬ жгучим видом, и поскольку по своей распространенности он относится к категории 2 (>1 особь/10 м2), то уровень опасности в этот день на данном пляже считается равным 3 (Встречаются ОЧЕНЬ ОПАСНЫЕ медузы).</p>
"""
            },
        },
    8: {
        'scientific_name': "Porpita porpita",
        'common_name': "Порпиты, синие кнопки",
        'photo': IMG_URL + "porpita.png",
        'description': """
<p>Данный вид обитает на поверхности океана, но зачастую особи бывают выброшены волнами на берег, где иногда встречаются в больших количествах. На побережье Каталонии эти медузы считаются редкими.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В случае Porpita porpita вид считается СЛЕГКА жгучим видом, уровень опасности 1 (Встречаются БЕЗОПАСНЫЕ медузы), вне зависимости от количества медуз на пляже, поскольку их присутствие не представляет опасности для купающихся.</p>
""",
            },
        },
    9: {
        'scientific_name': "Carybdea marsupialis",
        'common_name': "Кубомедуза",
        'photo': IMG_URL + "carybdea.png",
        'description': """
<p>Несмотря на то, что C. marsupialis относится к кубомедузам, ее яд не смертелен. В качестве места обитания эта медуза предпочитает песчаное дно, день она проводит на дне, а ночью перемещается к поверхности воды. Данный вид очень распространен в некоторых зонах испанского побережья Средиземного моря, но в каталонской части он считается редковстречающимся, хотя количество его особей может быть недооценено.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В данном случае вид Carybdea marsupialis считается ОЧЕНЬ жгучим видом, но поскольку по своей распространенности он относится к категории 1 (<1 особь/10 м2), то уровень опасности в этот день на данном пляже считается равным 2 (Встречаются ОПАСНЫЕ медузы).</p>
""",
            "VERY_HIGH_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В данном случае вид Carybdea marsupialis считается ОЧЕНЬ жгучим видом; поскольку по своей распространенности он относится к категории 2 (>1 особь/10 м2), то уровень опасности в этот день на данном пляже считается равным 3 (Встречаются ОЧЕНЬ ОПАСНЫЕ медузы.</p>
""",
            },
        },
    10: {
        'scientific_name': "Physalia physalis",
        'common_name': "Кубомедуза",
        'photo': IMG_URL + "physalia.png",
        'description': """
<p>Несмотря на то, что C. marsupialis относится к кубомедузам, ее яд не смертелен. В качестве места обитания эта медуза предпочитает песчаное дно, день она проводит на дне, а ночью перемещается к поверхности воды. Данный вид очень распространен в некоторых зонах испанского побережья Средиземного моря, но в каталонской части он считается редковстречающимся, хотя количество его особей может быть недооценено.</p>
""",
        'risk_description': {
            "VERY_HIGH_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В данном случае вид Carybdea marsupialis считается ОЧЕНЬ жгучим видом, и поскольку по своей распространенности он относится к категории 3 (>1 особь/м2), то уровень опасности в этот день на данном пляже считается равным 3 (Встречаются ОЧЕНЬ ОПАСНЫЕ медузы).</p>
""",
            },
        },
    11: {
        'scientific_name': "Olindias phosphorica",
        'common_name': "Фосфорический олиндиас",
        'photo': IMG_URL + "olindias.png",
        'description': """
<p>Время от времени встречается вдоль побережья Каталонии. Никогда не наблюдается больших групп, но в отдельных местах общее количество может быть значительным. В последние годы эти медузы очень распространены у средиземноморского берега Туниса, представляя собой проблему для индустрии туризма.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В данном случае вид Olindias phosphorica считается ОЧЕНЬ жгучим видом, но поскольку по своей распространенности он относится к категории 1 (<1 особь/10 м2), то уровень опасности в этот день на данном пляже считается равным 2 (Встречаются ОПАСНЫЕ медузы).</p>
""",
            "VERY_HIGH_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В данном случае вид Olindias phosphorica считается ОЧЕНЬ жгучим видом, и поскольку по своей распространенности он относится к категории 2 (>1 особь/10 м2), то уровень опасности в этот день на данном пляже считается равным 3 (Встречаются ОЧЕНЬ ОПАСНЫЕ медузы).</p>
"""
            },
        },
    12: {
        'scientific_name': "Mnemiopsis leidyi",
        'common_name': "Гребневик мнемиопсис",
        'photo': IMG_URL + "leidyi.png",
        'description': """
<p>Данный вид принадлежит к типу гребневиков, а не стрекающих, поэтому не имеет книдоцитов (стрекательных клеток) и не опасен для человека, однако наносит вред морским экосистемам, в которых появляется. Это инвазивный вид, о присутствии которого у берега Каталонии было сообщено впервые в 2009 году.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Уровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В случае Mnemiopsis leidyi вид считается НЕ жгучим видом, уровень опасности 1 (Встречаются БЕЗОПАСНЫЕ медузы), вне зависимости от количества медуз на пляже, поскольку их присутствие не представляет опасности для купающихся.</p>
""",
            },
        },
    13: {
        'scientific_name': "Phyllorhiza punctata",
        'common_name': "Пятнистая медуза",
        'photo': IMG_URL + "punctata.png",
        'description': """
<p>Эта медуза обитает у берега и в эстуариях, изначальный ареал обитания находится в Австралии и большей части Индо-Тихоокеанской области. Это инвазионный вид, о присутствии которого у берега Каталонии было сообщено впервые в 2010 году.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<pУровень опасности, связанный с наличием медуз на пляжах, выражается индексом, который складывается из токсичности вида и его распространенности в зоне купания. В случае Phyllorhiza punctata вид считается СЛЕГКА жгучим видом, уровень опасности 1 (Встречаются БЕЗОПАСНЫЕ медузы), вне зависимости от количества медуз на пляже, поскольку их присутствие не представляет опасности для купающихся.</p>
""",
            },
        },
    }