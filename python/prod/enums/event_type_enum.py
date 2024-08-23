from dataclasses import dataclass

@dataclass(frozen=True)
class EventTypeEnum:

    MINT: str = "mint"
    SWAP: str = "swap"
    BURN: str = "burn"
    SYNC: str = "sync"
    CREATE: str = "create" 

