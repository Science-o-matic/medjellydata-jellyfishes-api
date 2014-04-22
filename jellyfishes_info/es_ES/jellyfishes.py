# -*- coding: utf-8 -*-
from settings import NO_RISK, RISK, HIGH_RISK


JELLYFISHES = {
    1: {
        'scientific_name': "Pelagia noctiluca",
        'common_name': "Medusa luminiscente",
        'photo': "",
        'description': """
<p>Esta especie es considerada una de las más abundante e importantes a lo largo de la costa catalana.< Es una especie oceánica, por lo que su presencia en aguas costeras depende de las condiciones ambientales y climatológicas. Es muy frecuente en la época de primavera y verano, aún cuando su presencia se puede detectar durante todo el año.</p>
""",
        'risk_description': {
            RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En este caso, la especie Pelagia noctiluca es considerada una especie MUY urticante, pero debido a que su abundancia es de categoría 1 (<1 individuo / 10 m2), el nivel de peligrosidad específico para este día en esta playa es nivel 2 (Presencia de Medusas CON Peligro).</p>
""",
            HIGH_RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En este caso, la especie Pelagia noctiluca es considerada una especie MUY urticante y debido a que su abundancia es de categoría 2 (>1 individuo / 10 m2), el nivel de peligrosidad específico para este día en esta playa es nivel 3 (Presencia de Medusas ALTO Peligro).
"""
            },
        },
    2: {
        'scientific_name': "Rhizostoma pulmo",
        'common_name': "Acalefo azul",
        'photo': "",
        'description': """
<p>Es la medusa más grande de la costa Catalana (10-40 cm de diámetro). Es considerada una especie costera, presente generalmente en o cerca de la superficie. Es muy abundante a lo largo de la costa Catalana. Las medusas pequeñas se producen en primavera y los adultos de mayor tamaño son más evidentes en el verano y el comienzo del otoño.</p>
""",
        'risk_description': {
            NO_RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En este caso, la especie Rhizostoma pulmo es considerada una especie URTICANTE, pero debido a que su abundancia es de categoría 1 (<1 individuo / 10 m2), el nivel de peligrosidad específico para este día en esta playa es de nivel 1 (Presencia de Medusas SIN Peligro).
""",
            RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En
este caso, la especie Rhizostoma pulmo es considerada una especie URTICANTE, y debido a que su abundancia es de categoría 2 (>1 individuo / 10 m2), el nivel de peligrosidad específico para este día en esta playa es nivel 2 (Presencia de Medusas CON Peligro).</p>
"""
            }
        },
    3: {
        'scientific_name': "Aequorea forskalea",
        'common_name': "Medusa aequorea",
        'photo': "",
        'description': """
<p>Durante los últimos años se ha convertido en una especie frecuente en la costa Catalana, y cuando ocurre, lo hace en grandes números. Esta especie habita desde aguas templadas a tropicales, en áreas costeras y litorales, ocurriendo incluso de forma ocasional en mar abierto.</p>
""",
        'risk_description': {
            NO_RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En el caso de Aequorea forskalea al ser una especie LIGERAMENTE urticante, el nivel de peligrosidad es 1 (Presencia de medusas SIN peligro) independiente de la abundancia en la que esté presente en
la playa, ya que su presencia no representa ningún peligro para los bañistas.</p>
""",
            },
        },
    4: {
        'scientific_name': "Cotylorhiza tuberculata",
        'common_name': " Medusa huevo frito",
        'photo': "",
        'description': """
<p>Es una especie endémica del Mediterráneo y es muy frecuente en la costa Catalana. Es una especie costera, con preferencia de aguas más cálidas. Los adultos son más abundantes a finales del verano y principios de otoño.</p>
""",
        'risk_description': {
            NO_RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En el caso de Cotylorhiza tuberculata al ser una especie LIGERAMENTE urticante, el nivel de peligrosidad es 1 (Presencia de medusas SIN peligro) independiente de la abundancia en la que esté presente en la playa, ya que su presencia no representa ningún peligro para los bañistas.
""",
            },
        },
    5: {
        'scientific_name': "Velella velella",
        'common_name': "Vela púrpura (Barquetes de Sant Pere)",
        'photo': "",
        'description': """
<p>A lo largo de la costa Catalana, como en todo el Mediterráneo, es una especie muy frecuente especialmente durante la primavera. Vive en al interface agua/aire con el flotador sobre el agua. Puede estar presente en grandes enjambres alcanzando incluso varios kilómetros. Como su movimiento depende totalmente de las corrientes y de los vientos de superficie, pueden ser llevadas a la línea de costa y encontrarse varadas en las playas.</p>
""",
        'risk_description': {
            NO_RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En el caso de Velella velella al ser una especie LIGERAMENTE urticante, el nivel de peligrosidad es 1 (Presencia de medusas SIN peligro) independiente de la abundancia en la que esté presente en la playa, ya que su presencia no representa ningún peligro para los bañistas.</p>
""",
            },
        },
    6: {
        'scientific_name': "Aurelia aurita",
        'common_name': "Medusa luna",
        'photo': "",
        'description': """
<p>La frecuencia de esta especie a lo largo de la costa Catalana ha disminuido en los últimos años y actualmente es considerada una especie de baja frecuencia. Cuando está presente, puede ser observada al final de la primavera. Es una especie costera y se puede encontrar incluso en estuarios y puertos.</p>
""",
        'risk_description': {
            NO_RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En el caso de Aurelia aurita al ser una especie LIGERAMENTE urticante, el nivel de peligrosidad es 1 (Presencia de medusas SIN peligro) independiente de la abundancia en la que esté presente en la playa, ya que su presencia no representa ningún peligro para los bañistas.</p>
""",
            },
        },
    7: {
        'scientific_name': "Chrysaora hysoscella",
        'common_name': "Acalefo radiado",
        'photo': "",
        'description': """
<p>Es una especie pelágica relativamente grande (diámetro hasta 30 cm). A pesar de que puede ser bastante abundante en alguna áreas del Mediterráneo español, en la costa Catalana es considerada una especie poco frecuente y comúnmente presente en primavera.</p>
""",
        'risk_description': {
            RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En este caso, la especie Chrysaora hysoscella es considerada una especie MUY urticante, pero debido a que su abundancia es de categoría 1 (<1 individuo / 10 m2), el nivel de peligrosidad específico para este día en esta playa es nivel 2 (Presencia de Medusas CON Peligro).
""",
            HIGH_RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En este caso, la especie Chrysaora hysoscella es considerada una especie MUY urticante, y debido a que su abundancia es de categoría 2 (>1 individuo / 10 m2), el nivel de peligrosidad específico para este día en esta playa es nivel 3 (Presencia de Medusas ALTO Peligro).</p>
"""
            },
        },
    8: {
        'scientific_name': "Porpita porpita",
        'common_name': "Botón azul",
        'photo': "",
        'description': """
<p>Esta especie vive en la superficie del océano pero a veces son arrastrados hasta la orilla, donde puede ser vistos ocasionalmente de a miles. A lo largo de la costa Catalana esta especie es considerada rara.</p>
""",
        'risk_description': {
            NO_RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En el caso de Porpita porpita al ser una especie LIGERAMENTE urticante, el nivel de peligrosidad es 1 (Presencia de medusas SIN peligro) independiente de la abundancia en la que esté presente en la playa, ya que su presencia no representa ningún peligro para los bañistas.
""",
            },
        },
    9: {
        'scientific_name': "Carybdea marsupialis",
        'common_name': "Cubomedusa",
        'photo': "",
        'description': """
<p>A pesar de que C. marsupialis es una cubomedusa, su veneno no es letal.</p>
<p>El ambiente preferido de esta especie parece ser el substrato arenoso, y se localiza sobre el fondo durante el día desplazándose a la superficie durante la noche. Esta especie está presente en alta abundancia en algunas áreas de la costa Española Mediterránea, pero a lo largo de la costa Catalana es considerada muy rara, a pesar de que su presencia podría estar subestimada.</p>
""",
        'risk_description': {
            RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En este caso, la especie Carybdea marsupialis es considerada una especie MUY urticante, pero debido a que su abundancia es de categoría 1 (<1 individuo / 10 m2), el nivel de peligrosidad específico para este día en esta playa es nivel 2 (Presencia de Medusas CON Peligro).
""",
            HIGH_RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En este caso, la especie Carybdea marsupialis es considerada una especie MUY urticante, y debido a que su abundancia es de categoría 3 (>1 individuo / m2), el nivel de peligrosidad específico para este día en esta playa es nivel 3 (Presencia de Medusas ALTO Peligro).</p>
""",
            },
        },
    10: {
        'scientific_name': "Physalia physalis",
        'common_name': "Carabela portuguesa",
        'photo': "",
        'description': """
<p>Es una animal marino pelágico que flota en la superficie del mar y es arrastrada por los vientos y corrientes. Es más común en mar abierto, pero las corrientes y vientos pueden llevarlas a aguas poco profundas y costeras. En el Mediterráneo no se encuentra de forma frecuente y a lo largo de la costa Catalana es considerada muy rara, a pesar de que se han reportados algunas observaciones  aisladas en los últimos años.</p>
""",
        'risk_description': {
            HIGH_RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En este caso, la especie Physalia physalis es considerada una especie MUY urticante, por lo que el nivel de peligrosidad en la playa donde se encuentre es nivel 3 (Presencia de Medusas ALTO Peligro) independiente de la abundancia. Con la presencia de tan sólo un individuo de P. physalis a nivel de playa se considera una situación de peligro para los bañistas.
""",
            },
        },
    11: {
        'scientific_name': "Olindias phosphorica",
        'common_name': "Medusa cruz",
        'photo': "",
        'description': """
<p>La presencia de esta especie a lo largo de la costa Catalana es esporádica. Nunca se observan bancos extensos pero puede ser muy abundante localmente. En años recientes, está siendo muy abundante en la costa de Túnez en el Mediterráneo, causando problemas para la industria del turismo.</p>
""",
        'risk_description': {
            RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En este caso, la especie Olindias phosphorica es considerada una especie MUY urticante, pero debido a que su abundancia es de categoría 1 (<1 individuo / 10 m2), el nivel de peligrosidad específico para este día en esta playa es nivel 2 (Presencia de Medusas CON Peligro).
""",
            HIGH_RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En este caso, la especie Olindias phosphorica es considerada una especie MUY urticante, y debido a que su abundancia es de categoría 2 (>1 individuo / 10 m2), el nivel de peligrosidad específico para este día en esta playa es nivel 3 (Presencia de Medusas ALTO Peligro).</p>
"""
            },
        },
    12: {
        'scientific_name': "Olindias phosphorica",
        'common_name': "Medusa cruz",
        'photo': "",
        'description': """
<p>Esta especie no es un cnidario sino un ctenóforo, por lo que no tiene cnidocistos (células urticantes) y por tanto es inofensivo para los humanos, pero muy dañino para los ecosistemas marinos invadidos. Es una especie invasora que fue reportada por primera vez en la costa Catalana en el año 2009.</p>
""",
        'risk_description': {
            NO_RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En el caso de Mnemiopsis leidyi al ser una especie NO urticante, el nivel de peligrosidad es 1 (Presencia de medusas SIN peligro) independiente de la abundancia en la que esté presente en la playa, ya que su presencia no representa ningún peligro para los bañistas.
""",
            },
        },
    13: {
        'scientific_name': "Phyllorhiza punctata",
        'common_name': "Medusa de lunares blancos",
        'photo': "",
        'description': """
<>Esta especie es una medusa costera y de estuarios cuya distribución nativa incluye Australia y gran parte del Indo-Pacífico. Es una especie invasora, y fue reportada por primera vez en el año 2010 en el sur de la costa Catalana.
""",
        'risk_description': {
            NO_RISK: """
<p>El nivel de peligrosidad de la presencia de medusas en las playas se obtiene a través de un índice que considera la capacidad urticante propia de la especie y su abundancia en las aguas de baño. En el caso de Phyllorhiza punctata al ser una especie LIGERAMENTE urticante, el nivel de peligrosidad es 1 (Presencia de medusas SIN peligro) independiente de la abundancia en la que esté presente en la playa, ya que su presencia no representa ningún peligro para los bañistas.</p>
""",
            },
        },
    }
