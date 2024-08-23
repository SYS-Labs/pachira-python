# Copyright [2024] [Ian Moore]
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

from .record import Record

class SyncRecord(Record):
                  
    def apply(self, event, abi_load):
        pass