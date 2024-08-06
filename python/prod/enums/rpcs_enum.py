from dataclasses import dataclass
from .nets_enum import NetsEnum

DEFAULT_NET = NetsEnum.POLYGON

@dataclass(frozen=True)
class RPCEnum:
    
    def get_key(self, net = DEFAULT_NET):
        match net:
            case NetsEnum.POLYGON:
                select_key = 'JSON_RPC_POLYGON'
           
        return select_key 

    def get_rpc(self, net = DEFAULT_NET):
        match net:
            case NetsEnum.POLYGON:
                select_rpc = 'https://polygon-rpc.com'
           
        return select_rpc 