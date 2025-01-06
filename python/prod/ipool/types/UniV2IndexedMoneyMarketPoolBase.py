# Copyright [2024] [Ian Moore]
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

from uniswappy import *
from ..types import MoneyMarketPool
from ..utils import IndexedUniV2Utils
from ..types import MoneyMarketPool
from ..types import MoneyMarketSynthPool
from ..data import MoneyMarketPoolStruct

class UniV2IndexedMoneyMarketPoolBase(LPERC20):

    def __init__(self, mm_pool_name, address):
        super().__init__(mm_pool_name, address)
        self.pool = self._mmPool()
        self.mms_lp_tkn = None
        self.mms_x_tkn = None
        self.mms_y_tkn = None
        self.base_lp = None
        self.x_tkn = None
        self.y_tkn = None        
        self.manager = 'MM-LP' 
        
    def _mmPool(self):
        return MoneyMarketPoolStruct()
        
    def get_mms_tkn(self, tkn_in):

        if(tkn_in.token_name == self.x_tkn.token_name):
            return self.mms_x_tkn
        elif(tkn_in.token_name == self.y_tkn.token_name):
            return self.mms_y_tkn
        elif(tkn_in.token_name == self.mms_lp_tkn.token_name): 
            return self.mms_lp_tkn
            
    def _initUniV2IMMPool(self, base_lp: UniswapExchange, 
                          mms_lp: MoneyMarketSynthPool, 
                          manager: str = None, 
                          compoundingPercent: int = 100):

        lp_tkns = base_lp.factory.token_from_exchange[base_lp.name]
        self.x_tkn = lp_tkns[[*lp_tkns][0]]
        self.y_tkn = lp_tkns[[*lp_tkns][1]]
        self.base_lp = base_lp

        self.mms_lp_tkn = MoneyMarketSynthPool.MoneyMarketSynthPool(self.x_tkn.token_name+self.y_tkn.token_name)
        self.mms_x_tkn = MoneyMarketSynthPool.MoneyMarketSynthPool(self.x_tkn.token_name)
        self.mms_y_tkn = MoneyMarketSynthPool.MoneyMarketSynthPool(self.y_tkn.token_name)

        # goto: UniV2IndexedMoneyMarketPoolStorage.sol
        self.pool.COMPOUND_PERCENT = compoundingPercent;
        self.pool.manager = manager;
        self.pool.token0 = self.x_tkn
        self.pool.token1 = self.y_tkn

        # Lists
        self.pool.baseTokens.append(self.x_tkn.token_name);
        self.pool.baseTokens.append(self.y_tkn.token_name);

        self.pool.opposingTokenOfBase[self.y_tkn.token_name] = self.x_tkn.token_name
        self.pool.opposingTokenOfBase[self.x_tkn.token_name] = self.y_tkn.token_name
        self.pool.baseTokenOfMMLP[self.mms_x_tkn] = self.x_tkn.token_name
        self.pool.baseTokenOfMMLP[self.mms_y_tkn] = self.y_tkn.token_name
        self.pool.mmsOfBase[base_lp.token_name] = mms_lp.token_name
        self.pool.mmsOfBase[self.x_tkn.token_name] = self.mms_x_tkn
        self.pool.mmsOfBase[self.y_tkn.token_name] = self.mms_y_tkn

        # Initializations
        self.pool.lastBalOfToken[self.mms_lp_tkn] = 0
        
        self.pool.selfBalOfSynthPool[self.mms_lp_tkn] = 0
        self.pool.selfBalOfSynthPool[self.mms_x_tkn] = 0
        self.pool.selfBalOfSynthPool[self.mms_y_tkn] = 0

        self.pool.totalSharesOfMMSPool[self.token_name] = 0
        self.pool.totalSharesOfMMSPool[self.mms_lp_tkn] = 0
        self.pool.totalSharesOfMMSPool[self.mms_x_tkn] = 0
        self.pool.totalSharesOfMMSPool[self.mms_y_tkn] = 0

        self.pool.mmsBalanceOf[self.mms_lp_tkn] = {}
        self.pool.mmsBalanceOf[self.mms_lp_tkn][self.manager] = 0
        self.pool.mmsBalanceOf[self.mms_lp_tkn][self.token_name] = 0
        
        self.pool.mmsBalanceOf[self.mms_x_tkn] = {}
        self.pool.mmsBalanceOf[self.mms_x_tkn][self.token_name] = 0
        self.pool.mmsBalanceOf[self.mms_y_tkn] = {}
        self.pool.mmsBalanceOf[self.mms_y_tkn][self.token_name] = 0






        
    