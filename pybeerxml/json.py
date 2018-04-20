from .recipe import Recipe
from .style import Style
from .fermentable import Fermentable
from .hop import Hop
from .misc import Misc
from .mash import Mash
from .mash_step import MashStep
from .yeast import Yeast

import json

class BeerXMLtoJSONEncoder(json.JSONEncoder):
    def default(self, obj): # pylint: disable=E0202
        if isinstance(obj, (Recipe, Style, Fermentable, Hop, Mash, MashStep, Yeast, Misc)):
            data = obj.__dict__
            if isinstance(obj, Recipe):
                data['abv'] = obj.abv
                data['og_plato'] = obj.og_plato
                data['fg_plato'] = obj.fg_plato
                data['ibu'] = obj.ibu
                data['og'] = obj.og
                data['fg'] = obj.fg
            if isinstance(obj, Fermentable):
                data['add_after_boil'] = obj.add_after_boil
                data['ppg'] = obj.ppg
                data['addition'] = obj.addition
            return data
        return json.JSONEncoder.default(self, obj)
