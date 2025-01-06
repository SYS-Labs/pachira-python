# Copyright [2024] [Ian Moore]
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

class UniV2IndexedMoneyMarketPoolTokenVault():

    def __init__(self, mm_pool):
        self.mm_pool = mm_pool
        self.name = self.mm_pool.name

    def totalSupply(self):
        return self.mm_pool.totalSharesOfMMSPool[self.name];

    def balanceOf(self, user_nm):
        return self.mm_pool.mmsBalanceOf[self.name][user_nm];

    def transfer(self, from_adrr, to_addr, amt):
        self.mm_pool.mmsBalanceOf[self.name][from_adrr] -= amt;
        self.mm_pool.mmsBalanceOf[self.name][to_addr] += amt;


