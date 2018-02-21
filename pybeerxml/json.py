from .recipe import Recipe
from .style import Style
from .fermentable import Fermentable
from .hop import Hop
from .mash import Mash
from .mash_step import MashStep
from .yeast import Yeast

import json

class BeerXMLtoJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Recipe, Style, Fermentable, Hop, Mash, MashStep, Yeast)):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


