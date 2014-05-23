# -*- coding: utf-8 -*-
from settings import IMG_URL

JELLYFISHES = {
    1: {
        'scientific_name': "Pelagia noctiluca",
        'common_name': "Medusa luminosa",
        'photo': IMG_URL + "pelagia.png",
        'description': """
<p>Questa specie è considerata una delle più abbondanti e importanti lungo la costa catalana. Si tratta di una specie oceanica, per cui la sua presenza nelle acque costiere dipende dalle condizioni ambientali e climatologiche. È molto frequente in primavera ed estate, anche se la sua presenza può essere rilevata durante tutto l'anno.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. In questo caso, la specie Pelagia noctiluca è considerata MOLTO urticante, ma visto che la sua abbondanza è di categoria %(abundance)i %(abundance_ratio)s, il livello di pericolosità specifica per questo giorno in questa spiaggia è 2 (Presenza di meduse PERICOLOSE).
</p>
""",
            "VERY_HIGH_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. In questo caso, la specie Pelagia noctiluca è considerata MOLTO urticante e dato che la sua abbondanza è di categoria %(abundance)i %(abundance_ratio)s, il livello di pericolosità specifico per questo giorno in questa spiaggia è 3 (Presenza di meduse ALTAMENTE pericolose).
</p>
"""
            },
        },
    2: {
        'scientific_name': "Rhizostoma pulmo",
        'common_name': "Polmone di mare",
        'photo': IMG_URL + "rhizostoma.png",
        'description': """
<p>È la medusa più grande della costa catalana (10-40 cm di diametro). È considerata una specie costiera, presente generalmente in superficie o in prossimità della superficie. È molto abbondante lungo la costa catalana. Le meduse piccole si manifestano in primavera e gli esemplari adulti di maggior grandezza sono più evidenti in estate e all’inizio dell’autunno.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. In questo caso, la specie Rhizostoma pulmo è considerata URTICANTE, ma visto che la sua abbondanza è di categoria %(abundance)i %(abundance_ratio)s, il livello di pericolosità specifica per questo giorno in questa spiaggia è 1 (Presenza di meduse NON pericolose).</p>
""",
            "HIGH_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. In questo caso, la specie Rhizostoma pulmo è considerata URTICANTE, e dato che la sua abbondanza è di categoria %(abundance)i %(abundance_ratio)s, il livello di pericolosità specifica per questo giorno in questa spiaggia è 2 (Presenza di meduse PERICOLOSE).</p>
"""
            }
        },
    3: {
        'scientific_name': "Aequorea forskalea",
        'common_name': "Medusa aequorea",
        'photo': IMG_URL + "aequorea.png",
        'description': """
<p>Negli ultimi anni, è diventata una specie comune lungo la costa catalana e, quando è presente, lo è in gran numero. Questa specie vive in acque da temperate a tropicali, in aree costiere e litorali, e si trova occasionalmente anche in mare aperto.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. Nel caso dell’Aequorea forskalea, trattandosi di una specie LEGGERMENTE urticante, il livello di pericolosità è 1 (Presenza di meduse NON pericolose) indipendentemente dalla sua abbondanza sulla spiaggia, poiché la sua presenza non rappresenta pericolo alcuno per i bagnanti.</p>
""",
            },
        },
    4: {
        'scientific_name': "Cotylorhiza tuberculata",
        'common_name': "Cassiopea mediterranea",
        'photo': IMG_URL + "cotylorhiza.png",
        'description': """
<p>È una specie endemica del Mediterraneo ed è molto frequente lungo la costa catalana. È una specie costiera, che preferisce le acque più calde. Gli adulti sono molto abbondanti alla fine dell’estate e all’inizio dell’autunno.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. Nel caso della Cotylorhiza tuberculata, trattandosi di una specie LEGGERMENTE urticante, il livello di pericolosità è 1 (Presenza di meduse NON pericolose) indipendentemente dall’abbondanza sulla spiaggia, poiché la sua presenza non rappresenta rischio alcuno per i bagnanti.</p>
""",
            },
        },
    5: {
        'scientific_name': "Velella velella",
        'common_name': "Barchette di San Pietro",
        'photo': IMG_URL + "velella.png",
        'description': """
<p>Lungo la costa catalana, così come nel resto del Mediterraneo, è una specie molto frequente, soprattutto in primavera. Vive all’interfaccia acqua-aria con la ombrella sopra la superficie dell’acqua. Può essere presente in grandi banchi, lunghi anche diversi chilometri. Poiché i suoi movimenti dipendono totalmente dalle correnti e dai venti di superficie, può essere trasportata sul lungomare e arenarsi sulle spiagge.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. Nel caso della Velella velella, trattandosi di una specie LEGGERMENTE urticante, il livello di pericolosità è 1 (Presenza di meduse NON pericolose) indipendentemente dalla sua abbondanza sulla spiaggia, poiché la sua presenza non rappresenta pericolo alcuno per i bagnanti.</p>
""",
            },
        },
    6: {
        'scientific_name': "Aurelia aurita",
        'common_name': "Medusa quadrifoglio",
        'photo': IMG_URL + "aurelia.png",
        'description': """
<p>La frequenza di questa specie lungo la costa catalana è diminuita negli ultimi anni e attualmente è considerata una specie a bassa frequenza. Quando è presente, può essere osservata alla fine della primavera. È una specie costiera che si può trovare anche in estuari e porti.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. Nel caso dell’Aurelia aurita, trattandosi di una specie LEGGERMENTE urticante, il livello di pericolosità è 1 (Presenza di meduse NON pericolose) indipendentemente dalla sua abbondanza sulla spiaggia, poiché la sua presenza non rappresenta pericolo alcuno per i bagnanti.</p>
""",
            },
        },
    7: {
        'scientific_name': "Chrysaora hysoscella",
        'common_name': "Medusa bruna",
        'photo': IMG_URL + "chrysaora.png",
        'description': """
<p>È una specie pelagica relativamente grande (diametro fino a 30 cm). Nonostante la presenza piuttosto abbondante in alcune aree del Mediterraneo spagnolo, lungo la costa catalana è considerata una specie poco frequente e di solito presente in primavera.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. In questo caso, la specie Chrysaora hysoscella è considerata MOLTO urticante, ma visto che la sua abbondanza è di categoria %(abundance)i %(abundance_ratio)s, il livello di pericolosità specifica per questo giorno in questa spiaggia è 2 (Presenza di meduse PERICOLOSE).</p>
""",
            "VERY_HIGH_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. In questo caso, la specie Chrysaora hysoscella è considerata MOLTO urticante, e dato che la sua abbondanza è di categoria %(abundance)i %(abundance_ratio)s, il livello di pericolosità specifica per questo giorno in questa spiaggia è 3 (Presenza di meduse ALTAMENTE pericolose).</p>
"""
            },
        },
    8: {
        'scientific_name': "Porpita porpita",
        'common_name': "Bottone blu",
        'photo': IMG_URL + "porpita.png",
        'description': """
<p>Questa specie vive sulla superficie del mare, però a volte i suoi esemplari sono trascinati fino a riva, dove possono occasionalmente essere visti a migliaia. Lungo la costa catalana questa specie è considerata rara.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. Nel caso della Porpita porpita, trattandosi di una specie LEGGERMENTE urticante, il livello di pericolosità è 1 (Presenza di meduse NON pericolose) indipendentemente dalla sua abbondanza sulla spiaggia, poiché la sua presenza non rappresenta pericolo alcuno per i bagnanti.</p>
""",
            },
        },
    9: {
        'scientific_name': "Carybdea marsupialis",
        'common_name': "Cubomedusa",
        'photo': IMG_URL + "carybdea.png",
        'description': """
<p>Nonostante C. marsupialis sia una cubomedusa, il suo veleno non è letale. Il substrato sabbioso sembra essere l’ambiente preferito di questa medusa, che si posiziona sul fondo durante il giorno per spostarsi in superficie durante la notte. Questa specie è altamente presente in alcune aree della costa spagnola mediterranea, ma lungo la costa catalana è considerata molto rara, anche se la sua presenza potrebbe essere sottostimata.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. In questo caso, la specie Carybdea marsupialis è considerata MOLTO urticante, ma visto che la sua abbondanza è di categoria %(abundance)i %(abundance_ratio)s, il livello di pericolosità specifica per questo giorno in questa spiaggia è 2 (Presenza di meduse PERICOLOSE).</p>
""",
            "VERY_HIGH_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. In questo caso, la specie Carybdea marsupialis è considerata MOLTO urticante, e dato che la sua abbondanza è di categoria %(abundance)i %(abundance_ratio)s, il livello di pericolosità specifica per questo giorno in questa spiaggia è 3 (Presenza di meduse ALTAMENTE pericolose).</p>
""",
            },
        },
    10: {
        'scientific_name': "Physalia physalis",
        'common_name': "Caravella portoghese",
        'photo': IMG_URL + "physalia.png",
        'description': """
<p>Si tratta di un organismo pelagico che galleggia sulla superficie del mare e viene trascinato dai venti e dalle correnti. È più comune in mare aperto, pero le correnti e i venti possano trasportarla fino ad acque poco profonde e costiere. Nel Mediterraneo non è così frequente e lungo la costa catalana è considerata molto rara, anche se negli ultimi anni sono stati segnalati alcuni casi isolati.</p>
""",
        'risk_description': {
            "VERY_HIGH_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. In questo caso, la specie Physalia physalis è considerata MOLTO urticante, ragion per cui il livello di pericolosità delle spiagge dove è presente è 3 (Presenza di meduse ALTAMENTE pericolose) indipendentemente dalla sua abbondanza. La presenza anche di un unico esemplare di P. physalis a livello di spiaggia rappresenta una situazione di pericolo per i bagnanti.</p>
""",
            },
        },
    11: {
        'scientific_name': "Olindias phosphorica",
        'common_name': "Medusa olindia",
        'photo': IMG_URL + "olindias.png",
        'description': """
<p>La presenza di questa specie lungo la costa catalana è sporadica. Non si osservano mai banchi estesi, ma tale medusa può essere molto abbondante localmente. Negli ultimi anni è diventata molto frequente lungo la costa tunisina, causando problemi all’industria del turismo.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. In questo caso, la specie Olindias phosphorica è considerata MOLTO urticante, ma visto che la sua abbondanza è di categoria %(abundance)i %(abundance_ratio)s, il livello di pericolosità specifica per questo giorno in questa spiaggia è 2 (Presenza di meduse PERICOLOSE).</p>
""",
            "VERY_HIGH_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. In questo caso, la specie Olindias phosphorica è considerata MOLTO urticante, e dato che la sua abbondanza è di categoria %(abundance)i %(abundance_ratio)s, il livello di pericolosità specifica per questo giorno in questa spiaggia è 3 (Presenza di meduse ALTAMENTE pericolose).</p>
"""
            },
        },
    12: {
        'scientific_name': "Mnemiopsis leidyi",
        'common_name': "Noce di mare",
        'photo': IMG_URL + "leidyi.png",
        'description': """
<p>Questa specie non è del phylum degli cnidari, ma di quello dei ctenofori, pertanto non presenta cnidocisti (cellule urticanti) e quindi è innocua per gli esseri umani, ma molto dannosa per gli ecosistemi marini che ne sono invasi. Si tratta di una specie invasiva che è stata segnalata per la prima volta lungo la costa catalana nel 2009.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. Nel caso della Mnemiopsis leidyi, trattandosi di una specie NON urticante, il livello di pericolosità è 1 (Presenza di meduse NON pericolose) indipendentemente dalla sua abbondanza sulla spiaggia, poiché la sua presenza non rappresenta pericolo alcuno per i bagnanti.</p>
""",
            },
        },
    13: {
        'scientific_name': "Phyllorhiza punctata",
        'common_name': "Medusa maculata australiana",
        'photo': IMG_URL + "punctata.png",
        'description': """
<p>Si tratta di una specie di medusa costiera o di estuario, la cui distribuzione originaria copre l’Australia e gran parte dell’Indo-Pacifico. È una specie invasiva, che è stata segnalata per la prima volta al sud della costa catalana nel 2010.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Il livello di pericolosità della presenza di meduse sulle spiagge si calcola tramite un indice che prende in considerazione la capacità urticante propria della specie e la sua presenza nelle acque di balneazione. Nel caso della Phyllorhiza punctata, trattandosi di una specie LEGGERMENTE urticante, il livello di pericolosità è 1 (Presenza di meduse NON pericolose) indipendentemente alla sua abbondanza sulla spiaggia, poiché la sua presenza non rappresenta pericolo alcuno per i bagnanti.</p>
""",
            },
        },
    }
