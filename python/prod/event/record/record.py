# Copyright [2024] [Ian Moore]
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

from abc import *

class Record(ABC):
             
    @abstractmethod        
    def apply(self, event, abi_load):
        pass
