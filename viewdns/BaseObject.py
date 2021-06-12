class BaseObject:

    def __init__(self, *args, **kwargs):

        for attr in kwargs.keys():
            setattr(self, attr, kwargs[attr])

    def __str__(self):
        
        return "<{0}> {{{1}}}".format(self.__class__.__name__, (', '.join("%s=%s" % item for item in vars(self).items())))

    def __repr__(self):

        return str(self)
