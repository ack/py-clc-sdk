
class Server:

	def __init__(self, id, alias=None, **kw):
        self.id = id
        self.alias = alias
        self.__dict__.update(kw)

    
