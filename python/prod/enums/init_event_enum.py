from dataclasses import dataclass
from .event_type_enum import EventTypeEnum as EventType
from ..event.mint_event import MintEvent
from ..event.swap_event import SwapEvent
from ..event.burn_event import BurnEvent
from ..event.create_event import CreateEvent
from ..event.sync_event import SyncEvent

DEFAULT_EVENT = EventType.MINT

class InitEventEnum:
    
    def apply(self, connect, event_type = DEFAULT_EVENT):
        match event_type:
            case EventType.MINT:
                event = MintEvent(connect)
            case EventType.SWAP:
                event = SwapEvent(connect)     
            case EventType.BURN:
                event = BurnEvent(connect)         
            case EventType.SYNC:
                event = SyncEvent(connect)                         
           
        return event 