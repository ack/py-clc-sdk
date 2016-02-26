#from v1 import ClientV1
from v2 import ClientV2

class Config:
    VERIFY_SSL = False
    URI_V2 = "https://api.ctl.io"
    
    def __init__(self, **kw):
        self.__dict__.update(kw)
        
    @classmethod
    def default(cls, username, password, alias, *kw):
        return cls(
            username=username,
            password=password,
            alias=alias,
            verify_ssl=cls.VERIFY_SSL,
            uri_v2=cls.URI_V2,
        )

    
class Client:
    def __init__(self, config=None):
        self.config = config or Config.default()
        self.v2 = ClientV2(self.config)

