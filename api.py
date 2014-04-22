# MedJelly API interface module
import os
import settings
import random


class MedJellyAPI:

    @staticmethod
    def jellyfishes_by_beach(beach_id):
        """ Fake method returning random jellyfishes list """
        jellyfishes = []
        for n in range(random.randrange(1, 3)):
            jelly = {
                'id': random.randrange(1, 13),
                'risk_level': random.randrange(1, 3)
                }
            jellyfishes.append(jelly)

        return jellyfishes
