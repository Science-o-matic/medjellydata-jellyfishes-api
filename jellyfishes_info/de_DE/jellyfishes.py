# -*- coding: utf-8 -*-
from settings import IMG_URL


JELLYFISHES = {
    1: {
        'scientific_name': "Pelagia noctiluca",
        'common_name': "Leuchtqualle (auch Feuerqualle genannt)",
        'photo': IMG_URL + "pelagia.png",
        'description': """
<p>Diese Art gehört zu den an der katalanischen Küste am häufigsten vorkommenden Arten. Die Leuchtqualle ist eine Hochseeart, ihr Vorhandensein in Küstengewässern ist von den herrschenden Umwelt- und Klimabedingungen abhängig. Im Frühling und Sommer wird sie häufiger beobachtet, die wird jedoch auch gelegentlich in den anderen Jahreszeiten gesichtet.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Pelagia noctiluca ist eine Art mit VIEL Nesselgift, aufgrund der Menge ihres Auftretens gehört sie jedoch zur Kategorie 1 (< 1 Tier / 10 m2), das Gefährdungspotenzial für den heutigen Tag an diesem Strand beträgt daher Niveau 2 (Vorhandensein von Quallen MIT Gefährdung).</p>
""",
            "VERY_HIGH_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Pelagia noctiluca ist eine Art mit VIEL Nesselgift, aufgrund der Menge ihres Auftretens gehört sie zur Kategorie 2 (> 1 Tier / 10 m2), das Gefährdungspotenzial für den heutigen Tag an diesem Strand beträgt daher Niveau 3 (Vorhandensein von Quallen MIT STARKER Gefährdung).</p>
"""
            },
        },
    2: {
        'scientific_name': "Rhizostoma pulmo",
        'common_name': "Wurzelmundqualle (auch Blumenkohlqualle genannt)",
        'photo': IMG_URL + "rhizostoma.png",
        'description': """
<p>Dies ist die größte an der katalanischen Küste vorkommende Qualle (10-40 cm Durchmesser). Es handelt sich um eine Küstenart, die in der Regel an der Oberfläche oder in der Nähe der Oberfläche vorkommt. Sie ist an der gesamten katalanischen Küste weit verbreitet. Im Frühling treten die kleinen Quallen auf, die ausgewachsenen Quallen sind im Sommer und Anfang Herbst häufiger.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Rhizostoma pulmo ist eine Art mit NESSELGIFT, aufgrund der Menge ihres Auftretens gehört sie jedoch zur Kategorie 1 (< 1 Tier / 10 m2), das Gefährdungspotenzial für den heutigen Tag an diesem Strand beträgt daher Niveau 1 (Vorhandensein von Quallen OHNE Gefährdung).</p>
""",
            "HIGH_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Rhizostoma pulmo ist eine Art mit NESSELGIFT, aufgrund der Menge ihres Auftretens gehört sie zur Kategorie 2 (> 1 Tier / 10 m2), das Gefährdungspotenzial für den heutigen Tag an diesem Strand beträgt daher Niveau 2 (Vorhandensein von Quallen MIT Gefährdung).</p>
"""
            }
        },
    3: {
        'scientific_name': "Aequorea forskalea",
        'common_name': "Aequorea-Qualle",
        'photo': IMG_URL + "aequorea.png",
        'description': """
<p>In den vergangenen Jahren ist diese Art an der katalanischen Küste zu einer häufig vertretenen Art geworden, und wenn sie auftritt, dann in großen Mengen. Diese Art lebt in warmen bis tropischen Gewässern in küstennahen Gewässern, wurde aber auch schon auf offener See gesichtet.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Aequorea forskalea ist eine Art mit SCHWACHEM Nesselgift, ihr Gefährdungspotenzial beträgt Niveau 1 (Vorhandensein von Quallen OHNE Gefährdung), dies ist unabhängig von der Menge ihres Auftretens, da diese Quallenart keine Gefährdung für Badende darstellt.</p>
""",
            },
        },
    4: {
        'scientific_name': "Cotylorhiza tuberculata",
        'common_name': "Spiegeleiqualle",
        'photo': IMG_URL + "cotylorhiza.png",
        'description': """
<p>Es handelt sich um eine für das Mittelmeer endemische Art, die an der katalanischen Küste sehr häufig vorkommt. Die Küstenart bevorzugt wärmere Gewässer. Die ausgewachsenen Quallen sind Ende Sommer und Anfang Herbst häufiger.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Cotylorhiza tuberculata ist eine Art mit SCHWACHEM Nesselgift, ihr Gefährdungspotenzial beträgt Niveau 1 (Vorhandensein von Quallen OHNE Gefährdung), dies ist unabhängig von der Menge ihres Auftretens, da diese Quallenart keine Gefährdung für Badende darstellt.</p>
""",
            },
        },
    5: {
        'scientific_name': "Velella velella",
        'common_name': "Segelqualle",
        'photo': IMG_URL + "velella.png",
        'description': """
<p>Diese Art ist im gesamten Mittelmeerraum und auch an der katalanischen Küste sehr häufig anzutreffen, besonders im Frühling. Sie treibt zwischen Wasser und Luft auf dem Meer. Sie kann in  großen Schwärmen auftreten, die sich über mehrere Kilometer erstrecken können. Sie bewegt sich ausschließlich mit der Strömung des Meeres und dem Meer und kann daher an die Küste getrieben werden und an den Stränden liegen bleiben.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Velella velella ist eine Art mit SCHWACHEM Nesselgift, ihr Gefährdungspotenzial beträgt Niveau 1 (Vorhandensein von Quallen OHNE Gefährdung), dies ist unabhängig von der Menge ihres Auftretens, da diese Quallenart keine Gefährdung für Badende darstellt.</p>
""",
            },
        },
    6: {
        'scientific_name': "Aurelia aurita",
        'common_name': "Ohrenqualle",
        'photo': IMG_URL + "aurelia.png",
        'description': """
<p>Das Vorkommen dieser Art an der katalanischen Küste hat in den vergangenen Jahren immer weiter abgenommen, heute gilt diese Art als selten vertretene Art. Wenn überhaupt kann man sie Ende Frühling beobachten. Die Küstenart ist auch in Mündungsgebieten und Hafenbecken anzutreffen.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Aurelia aurita ist eine Art mit SCHWACHEM Nesselgift, ihr Gefährdungspotenzial beträgt Niveau 1 (Vorhandensein von Quallen OHNE Gefährdung), dies ist unabhängig von der Menge ihres Auftretens, da diese Quallenart keine Gefährdung für Badende darstellt.</p>
""",
            },
        },
    7: {
        'scientific_name': "Chrysaora hysoscella",
        'common_name': "Kompassqualle",
        'photo': IMG_URL + "chrysaora.png",
        'description': """
<p>Diese Quallenart ist relativ groß (Durchmesser bis 30 cm). Diese Art kommt an den spanischen Mittelmeerküsten zwar teilweise in großen Mengen vor, an der katalanischen Küste kommt sie jedoch ziemlich selten vor und wenn meistens im Frühling.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Chrysaora hysoscella ist eine Art mit VIEL Nesselgift, aufgrund der Menge ihres Auftretens gehört sie jedoch zur Kategorie 1 (< 1 Tier / 10 m2), das Gefährdungspotenzial für den heutigen Tag an diesem Strand beträgt daher Niveau 2 (Vorhandensein von Quallen MIT Gefährdung).</p>
""",
            "VERY_HIGH_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Chrysaora hysoscella ist eine Art mit VIEL Nesselgift, aufgrund der Menge ihres Auftretens gehört sie zur Kategorie 2 (> 1 Tier / 10 m2), das Gefährdungspotenzial für den heutigen Tag an diesem Strand beträgt daher Niveau 3 (Vorhandensein von Quallen MIT STARKER Gefährdung).</p>
"""
            },
        },
    8: {
        'scientific_name': "Porpita porpita",
        'common_name': "Porpita porpita Qualle",
        'photo': IMG_URL + "porpita.png",
        'description': """
<p>Diese Ozeanart lebt an der Meeresoberfläche, wird jedoch zuweilen ans Ufer geschwemmt, wo sich gelegentlich Tausende dieser Quallen ansammeln. Diese Art ist an der katalanischen Küste selten.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Porpita porpita ist eine Art mit SCHWACHEM Nesselgift, ihr Gefährdungspotenzial beträgt Niveau 1 (Vorhandensein von Quallen OHNE Gefährdung), dies ist unabhängig von der Menge ihres Auftretens, da diese Quallenart keine Gefährdung für Badende darstellt.</p>
""",
            },
        },
    9: {
        'scientific_name': "Carybdea marsupialis",
        'common_name': "Würfelqualle",
        'photo': IMG_URL + "carybdea.png",
        'description': """
<p>Die C. marsupialis ist zwar eine Würfelqualle, ihr Nesselgift ist jedoch nicht lebensgefährlich. Diese Art bevorzugt den Sandboden als Lebensraum und hält sich tagsüber auf dem Meeresboden auf und bewegt sich nachts fort. Diese Art kommt an in einigen Bereichen der spanischen Mittelmeerküste zwar teilweise in großen Mengen vor, an der katalanischen Küste gilt sie jedoch als sehr selten, ihr Vorkommen könnte jedoch unterschätzt werden.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Carybdea marsupialis ist eine Art mit VIEL Nesselgift, aufgrund der Menge ihres Auftretens gehört sie jedoch zur Kategorie 1 (< 1 Tier / 10 m2), das Gefährdungspotenzial für den heutigen Tag an diesem Strand beträgt daher Niveau 2 (Vorhandensein von Quallen MIT Gefährdung).</p>
""",
            "VERY_HIGH_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Carybdea marsupialis ist eine Art mit VIEL Nesselgift, aufgrund der Menge ihres Auftretens gehört sie zur Kategorie 2 (> 1 Tier / 10 m2 diesem), das Gefährdungspotenzial für den heutigen Tag an Strand beträgt daher Niveau 3 (Vorhandensein von Quallen MIT STARKER Gefährdung).</p>
""",
            },
        },
    10: {
        'scientific_name': "Physalia physalis",
        'common_name': "Portugiesische Galeere",
        'photo': IMG_URL + "physalia.png",
        'description': """
<p>Es handelt sich um eine Art aus der Gattung der Seeblasen, die an der Meeresoberfläche lebt und vom Wind und der Strömung bewegt wird. Sie lebt üblicherweise auf offener See, kann jedoch von der Strömung und dem Wind in flache und küstennahe Zonen getrieben werden. Im Mittelmeer kommt sie nicht häufig vor, und an der katalanischen Küste gilt sie als sehr selten, wurde jedoch in den vergangenen Jahren vereinzelt gesichtet.</p>
""",
        'risk_description': {
            "VERY_HIGH_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Physalia physalis ist eine Art mit VIEL Nesselgift, das Gefährdungspotenzial an Stränden, an denen die Art beobachtet wird, beträgt unabhängig von der Menge ihres Auftretens immer Niveau 3 (Vorhandensein von Quallen MIT STARKER Gefährdung). Schon das Vorhandensein einer einzigen Qualle der Art P. physalis in Strandnähe kann die Badenden gefährden.</p>
""",
            },
        },
    11: {
        'scientific_name': "Olindias phosphorica",
        'common_name': "Kreuzqualle",
        'photo': IMG_URL + "olindias.png",
        'description': """
<p>Diese Art kommt an der katalanischen Küste nur sporadisch vor. Große Quallenbänke werden nie beobachtet, lokal kann die Quallenart jedoch zahlreich auftreten. In den vergangenen Jahren wurde die Art in großen Mengen an der tunesischen Mittelmeerküste beobachtet, was dem Tourismus in der Region geschadet hat.</p>
""",
        'risk_description': {
            "HIGH_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Olindias phosphorica ist eine Art mit VIEL Nesselgift, aufgrund der Menge ihres Auftretens gehört sie jedoch zur Kategorie 1 (< 1 Tier / 10 m2), das Gefährdungspotenzial für den heutigen Tag an diesem Strand beträgt daher Niveau 2 (Vorhandensein von Quallen MIT Gefährdung).</p>
""",
            "VERY_HIGH_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Olindias phosphorica ist eine Art mit VIEL Nesselgift, aufgrund der Menge ihres Auftretens gehört sie zur Kategorie 2 (> 1 Tier / 10 m2), das Gefährdungspotenzial für den heutigen Tag an diesem Strand beträgt daher Niveau 3 (Vorhandensein von Quallen MIT STARKER Gefährdung).</p>
"""
            },
        },
    12: {
        'scientific_name': "Mnemiopsis leidyi",
        'common_name': "Meerwalnuss",
        'photo': IMG_URL + "leidyi.png",
        'description': """
<p>Diese Art ist eine Rippenquallen (Ctenophora) und kein Nesseltier. Sie hat daher keine Nesselzellen (Cnidozyten) und ist für den Menschen harmlos, jedoch sehr schädlich für das marine Ökosystem. Es handelt sich um eine invasive Spezies, die 2009 zum ersten Mal an der katalanischen Küste gesichtet wurde.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Mnemiopsis leidyi ist eine Art OHNE Nesselgift, ihr Gefährdungspotenzial beträgt Niveau 1 (Vorhandensein von Quallen OHNE Gefährdung), dies ist unabhängig von der Menge ihres Auftretens, da diese Quallenart keine Gefährdung für Badende darstellt.</p>
""",
            },
        },
    13: {
        'scientific_name': "Phyllorhiza punctata",
        'common_name': "Gepunktete Wurzelmundqualle",
        'photo': IMG_URL + "punctata.png",
        'description': """
<p>Diese Art kommt an der Küste und in Mündungsbereichen vor und stammt ursprünglich aus Australien und dem Bereich Indischer Ozean/Pazifischer Ozean. Es handelt sich um eine invasive Spezies, die 2010 zum ersten Mal an der katalanischen Küste gesichtet wurde.</p>
""",
        'risk_description': {
            "LOW_WARNING": """
<p>Das Gefährdungspotenzial von Quallen an Stränden wird mit einem Index angegeben, der sich aus der Gefährdung durch das Nesselgift der Art und ihrem Vorkommen in den Badegewässern ergibt. Die Phyllorhiza punctata ist eine Art mit SCHWACHEM Nesselgift, ihr Gefährdungspotenzial beträgt Niveau 1 (Vorhandensein von Quallen OHNE Gefährdung), dies ist unabhängig von der Menge ihres Auftretens, da diese Quallenart keine Gefährdung für Badende darstellt.</p>
""",
            },
        },
    }
