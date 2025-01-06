# Copyright [2024] [Ian Moore]
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

from uniswappy import *

class MoneyMarketSynthPool(LPERC20):
    
    def __init__(self, pool_name, address = None):
        super().__init__(pool_name, address)


