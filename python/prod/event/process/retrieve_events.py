from ...abi.abi_loading import ABILoading
from ...enums.init_event_enum import InitEventEnum as InitEvent
from ...utils.connect import ConnectW3
from ..event import Event
from ..tools.log_result import LogResult
from ..tools.rpc_reorganization_monitor import JSONRPCReorganizationMonitor
from .read_events import ReadEvents

class RetrieveEvents:

    def __init__(self, connect: ConnectW3, abi: ABILoading, verbose = True):
        self.__connect = connect   
        self.__abi = abi 
        self.__w3 = self.__connect.get_w3()
        self.__contract = self.get_contract()
        self.__verbose = verbose
    
    def apply(self, event_type, start_block = None, end_block = None):

        event = InitEvent().apply(self.__connect, event_type)
        read_events = self.gen_read_events(event, start_block, end_block)
        processed_events = set()
        dict_events = {}
        evt: LogResult
        for k, evt in enumerate(read_events):
            key = evt["blockHash"] + evt["transactionHash"] + evt["logIndex"]        
            record_event = event.record(evt, self.__abi)
               
            dict_events[k] = record_event
            if key not in processed_events:
                if(self.__verbose): print(f"Swap at block:{evt['blockNumber']:,} tx:{evt['transactionHash']}")
                processed_events.add(key)
        else:
            if(self.__verbose): print(".")

        return dict_events        

    def gen_read_events(self, event, start_block = None, end_block = None):
        self.__w3.middleware_onion.clear()
        s_block = 1 if start_block == None else start_block
        e_block = self.latest_block() if end_block == None else end_block
        event_filt = event.filter(self.__contract)
        read_events = ReadEvents().apply(self.__w3, start_block=s_block, end_block=e_block, filter=event_filt)   
        return read_events

    def get_contract(self):
        return self.__abi.apply(self.__w3)
    
    def latest_block(self):
        reorg_mon = JSONRPCReorganizationMonitor(self.__w3, check_depth=3)
        reorg_mon.load_initial_block_headers(block_count=5)
        return reorg_mon.get_last_block_live()