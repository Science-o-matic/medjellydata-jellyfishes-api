# -*- coding: utf-8 -*-
from settings import NO_RISK, RISK, HIGH_RISK, IMG_URL


JELLYFISHES = {
    1: {
        'scientific_name': "Pelagia noctiluca",
        'common_name': "Mauve stinger",
        'photo': IMG_URL + "pelagia.png",
        'description': """
<p>This species is considered one of the most important and abundant along the Catalan coast. It is an offshore species, therefore its presence in coastal waters depends on the environmental and weather conditions. It occurs very frequently in spring and summer, although they may reach the coastline in any season of the year.</p>
""",
        'risk_description': {
            RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In this case, the species Pelagia noctiluca is considered as HIGH stinging, but due to an abundance category 1 (<1 individual / 10 m2), the specific risk level for today at this beach is level 2 (Jellyfish Presence WITH risk)</p>
""",
            HIGH_RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In this case, the species Pelagia noctiluca is considered as HIGH stinging, and due to an abundance category 2 (>1 individual / 10 m2), the specific risk level for today at this beach is level 3 (Jellyfish Presence with HIGH risk)
"""
            },
        },
    2: {
        'scientific_name': "Rhizostoma pulmo",
        'common_name': "Barrel jellyfish",
        'photo': IMG_URL + "rhizostoma.png",
        'description': """
<p>It is the biggest jellyfish on the Catalan coast (10-40 cm diameter). It is considered a coastal species, usually recorded at or near the water surface, and it lives in abundance along the Catalan coast. The small jellies are produced in spring and the big adults are more evident in summer and early autumn.</p>
""",
        'risk_description': {
            NO_RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In this case, the species Rhizostoma pulmo is considered as STINGING, but due to an abundance category 1 (<1 individual / 10 m2), the specific risk level for today at this beach is level 1 (Jellyfish Presence with NO risk)
""",
            RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In this case, the species Rhizostoma pulmo is considered as STINGING, and due to an abundance category 2 (>1 individual / 10 m2), the specific risk level for today at this beach is level 2 (Jellyfish Presence WITH risk)
"""
            }
        },
    3: {
        'scientific_name': "Aequorea forskalea",
        'common_name': "Many-ribbed jellyfish",
        'photo': IMG_URL + "aequorea.png",
        'description': """
<p>During recent years it has become a frequent species on the Catalan coast, and when it occurs, it is in large numbers. This species inhabits temperate to tropical waters, coastal and offshore areas, even occurring occasionally in mid-ocean.</p>
""",
        'risk_description': {
            NO_RISK: """
<p<The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In the case of Aequorea forskalea as it is a MILD/LOW stinging species; the risk level is 1 (Jellyfish presence with NO risk) independent of the abundance present at the beach, because its presence does not represent anyrisk for bathers.</p>
""",
            },
        },
    4: {
        'scientific_name': "Cotylorhiza tuberculata",
        'common_name': "Fried egg jellyfish",
        'photo': IMG_URL + "cotylorhiza.png",
        'description': """
<p>It is an endemic species in the Mediterranean and it is very frequent on the Catalan coast. It is a coastal species, showing some preference for warmer waters. Adults are seen in highest abundances in late summer and early autumn.</p>
""",
        'risk_description': {
            NO_RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In the case of Cotylorhiza tuberculata as it is a MILD/LOW stinging species; the risk level is 1 (Jellyfish presence with NO risk) independent of the abundance present at the beach, because its presence does not represent any risk for bathers.</p>
""",
            },
        },
    5: {
        'scientific_name': "Velella velella",
        'common_name': "By-the-wind sailor",
        'photo': IMG_URL + "velella.png",
        'description': """
<p>Along the Catalan coast, as in the whole Mediterranean basin, it occurs very frequently especially during springtime. It lives in the water/air interface, with the float above the water. It may be present in huge swarms reaching even several kilometres. As their movement depends totally on currents and surface winds, they can be blown to the coast and be found stranded on the beaches.</p>
""",
        'risk_description': {
            NO_RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In the case of Velella velella as it is a MILD/LOW stinging species; the risk level is 1 (Jellyfish presence with NO risk) independent of the abundance present at the beach, because its presence does not represent any risk for bathers.</p>
""",
            },
        },
    6: {
        'scientific_name': "Aurelia aurita",
        'common_name': "Moon jellyfish",
        'photo': IMG_URL + "aurelia.png",
        'description': """
<p>The frequency of this species along the Catalan coast has decreased in recent years, and now considered a low frequency species. When present, it can be often observed at the end of the spring season. It is an inshore species and can even be found in estuaries and harbours.</p>
""",
        'risk_description': {
            NO_RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In the case of Aurelia aurita as it is a MILD/LOW stinging species; the risk level is 1 (Jellyfish presence with NO risk) independent of the abundance present at the beach, because its presence does not represent any risk for bathers.</p>
""",
            },
        },
    7: {
        'scientific_name': "Chrysaora hysoscella",
        'common_name': "Compass jellyfish",
        'photo': IMG_URL + "chrysaora.png",
        'description': """
<p>It is a quite big (diameter up to 30 cm) pelagic species. Although it may be very abundant in some Spanish Mediterranean areas, on the Catalan coast it is considered a low frequency species and it is mostly observed in spring.</p>
""",
        'risk_description': {
            RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In this case, the species Chrysaora hysoscella is considered as HIGH stinging, but due to an abundance category 1 (<1 individual / 10 m2), the specific risk level for today at this beach is level 2 (Jellyfish Presence WITH risk)</p>
""",
            HIGH_RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In this case, the species Chrysaora hysoscella is considered as HIGH stinging, and due to an abundance category 2 (>1 individual / 10 m2), the specific risk level for today at this beach is level 3 (Jellyfish Presence with HIGH risk)</p>
"""
            },
        },
    8: {
        'scientific_name': "Porpita porpita",
        'common_name': "Blue button",
        'photo': IMG_URL + "porpita.png",
        'description': """
<p>This species live on the ocean surface, but are sometimes blown into shore, and occasionally seen by thousands. Along the Catalan coast this species is very rare.</p>
""",
        'risk_description': {
            NO_RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In the case of Porpita porpita as it is a MILD/LOW stinging species; the risk level is 1 (Jellyfish presence with NO risk) independent of the abundance present at the beach, because its presence does not represent any risk for bathers.</p>
""",
            },
        },
    9: {
        'scientific_name': "Carybdea marsupialis",
        'common_name': "Box jellyfish",
        'photo': IMG_URL + "carybdea.png",
        'description': """
<p>Although C. marsupialis is a cubozoan, its poison is not lethal.</p>
<p>The preferred habitat of this species appears to be over sandy substrate, located just above the bottom during the day and moving up toward the surface at night. This species is present in high abundances in some areas of the Spanish Mediterranean coast, but along the Catalan coast it is considered very rare, although its presence may be underestimated more than absent.</p>
""",
        'risk_description': {
            RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In this case, the species Carybdea marsupialis is considered as HIGH stinging, but due to an abundance category 1 (<1 individual / 10 m2), the specific risk level for today at this beach is level 2 (Jellyfish Presence WITH risk)</p>
""",
            HIGH_RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In this case, the species Carybdea marsupialis is considered as HIGH stinging, and due to an abundance category 2 (>1 individual / 10 m2), the specific risk level for today at this beach is level 3 (Jellyfish Presence with HIGH risk)</p>
""",
            },
        },
    10: {
        'scientific_name': "Physalia physalis",
        'common_name': "Portuguese Man-of-War",
        'photo': IMG_URL + "physalia.png",
        'description': """
<p>It is a pelagic marine animal that floats in the surface of the sea and it is blown about by the winds and pushed around by the currents. It is most common in the open ocean, but currents and winds may direct them into shallow waters or wash them up on beaches. In the Mediterranean it is not encountered frequently and along the Catalan coast it is considered very rare, although some isolated observations have been reported in recent years.</p>
""",
        'risk_description': {
            HIGH_RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In this case, the species Physalia physalis is considered a HIGH stinging species, therefore the risk level in the beach where it is present is level 3 (Jellyfish Presence with HIGH risk) independent of the abundance. With the presence of only one individual of P. physalis at the beach it is considered a high-risk situation for bathers.</p>
""",
            },
        },
    11: {
        'scientific_name': "Olindias phosphorica",
        'common_name': "Cigar jellyfish",
        'photo': IMG_URL + "olindias.png",
        'description': """
<p>The presence of these jellyfish along the Catalan coast is sporadic. It never forms extended swarms, but can be locally abundant. In recent years, it has been very abundant along the coasts of Tunisia in the Mediterranean, causing problems for the tourism industry.</p>
""",
        'risk_description': {
            RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In this case, the species Olindias phosphorica is considered as HIGH stinging, but due to an abundance category 1 (<1 individual / 10 m2), the specific risk level for today at this beach is level 2 (Jellyfish Presence WITH risk)</p>
""",
            HIGH_RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In this case, the species Olindias phosphorica is considered as HIGH stinging, and due to an abundance category 2 (>1 individual / 10 m2), the specific risk level for today at this beach is level 3 (Jellyfish Presence with HIGH risk)</p>
"""
            },
        },
    12: {
        'scientific_name': "Mnemiopsis leidyi",
        'common_name': "Sea walnut, comb jelly",
        'photo': IMG_URL + "leidyi.png",
        'description': """
<p>As it is not a cnidarian, but a ctenophore, so it doesn’t have cnidocysts and therefore it is not poisonous. It is harmless to humans, but very harmful to the invaded marine ecosystems. It is an invasive species that was first reported on the Catalan coast in the year 2009.</p>
""",
        'risk_description': {
            NO_RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In the case of Mnemiopsis leidyi as it is a HARMLESS species; the risk level is 1 (Jellyfish presence with NO risk) independent of the abundance present at the beach, because its presence does not represent any risk for bathers.
""",
            },
        },
    13: {
        'scientific_name': "Phyllorhiza punctata",
        'common_name': "Australian White Spotted jellyfish",
        'photo': IMG_URL + "punctata.png",
        'description': """
<p>This species is a coastal and estuarine jellyfish whose wide native distribution includes Australia and much of the Indo-Pacific. It is an invasive species, and was first reported on the southern Catalan coast in the year 2010.</p>
""",
        'risk_description': {
            NO_RISK: """
<p>The risk level of jellyfish presence at the beaches is determined though an index that considers the stinging level of the species and the abundance in bathing waters. In the case of Phyllorhiza punctata as it is a MILD/LOW stinging species; the risk level is 1 (Jellyfish presence with NO risk) independent of the abundance present at the beach, because its presence does not represent any risk for bathers.</p>
""",
            },
        },
    }
