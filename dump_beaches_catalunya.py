import os
import jellyfishes_info

# 'ca_ES', 'es_ES', 'en_EN', 'de_DE', 'fr_FR', 'it_IT', 'ru_RU'
jellyfishes_info.beaches_catalunya(os.getenv("LANG"), stdout=True)
