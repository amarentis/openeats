# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from measurement.measures import Volume, Weight


def mass_to_volume_lookup(mass, ingredient):
    """
    Given a
        - Weight object (kg, g, etc...),
        - ingredient (flour, sugar, etc...)
    Return the mass to volume ratio
    """

    # Convert volume to liter

    # Convert mass to kilogram


    # ratios for 1 gram to 1 cup
    ratios = {
        'flour': 1,
    }

    try:
        ratio = ratios[ingredient.lower()]
    except:
        ratio = 1

    return Volume(us_cup=(mass.g * ratio))
