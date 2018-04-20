class Misc(object):
    def __init__(self):
        self.name = None
        self.type = None
        self.use = None
        self.time = None
        self.amount = None
        self.amount_is_weight = None
        self.use_for = None
        self.notes = None

    def __repr__(self):
        return 'pybeerxml.Misc<{}>'.format(self.name)