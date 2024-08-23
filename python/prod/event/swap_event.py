# Copyright [2024] [Ian Moore]
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

from .event import Event

class SwapEvent(Event):
                        
    def record(self, event, abi_load):
        pass
     
    def filter(self, contract):
        pass