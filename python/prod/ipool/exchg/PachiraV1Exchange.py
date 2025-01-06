# Copyright [2024] [Ian Moore]
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

from ..utils import IndexedUniV2Utils
from ..types import MoneyMarketSynthPool
from ..types import UniV2IndexedMoneyMarketPoolBase
from ..calc import SaferMath
from uniswappy import *
import math

PROVIDER_PROTOCOL = 'protocol_owner'

class PachiraV1Exchange():
    
    def __init__(self, base_lp, mmPool = None, mmsPool = None):
        self.mm = UniV2IndexedMoneyMarketPoolBase('MM', address="0x012")
        self.mms = MoneyMarketSynthPool('SYNTH', address="0x011")
        self.base_lp = base_lp
        self.name = base_lp.name
        self.mm._initUniV2IMMPool(self.base_lp, self.mms)

    def summary(self):
        self.base_lp.summary()

    ## **************************** Solidity Refactored **************************** ##

    def exchangein_basein_yieldout(self, token_in, token_out, amount_in, recipient):

        SwapDeposit().apply(self.base_lp, token_in, recipient, amount_in)
        amount_out = self.base_lp.last_liquidity_deposit
        
        return amount_out

    def exchangein_yieldin_baseout(self, token_in, token_out, amount_in, recipient):

        # tkn_amount_remove = self.calc_dx(self.base_lp, token_out, amount_in)
        # opp_tkn = self.get_opp_tkn(self.base_lp, token_out)
        # out1 = RemoveLiquidity().apply(self.base_lp, token_out, recipient, tkn_amount_remove) 
        # out2 = Swap().apply(self.base_lp, opp_tkn, recipient, out1[opp_tkn.token_name])
        # amount_out = out2 + out1[token_out.token_name]

        tkn_amt_out = LPQuote(False).get_amount_from_lp(self.base_lp, token_out, amount_in)
        amount_out = WithdrawSwap().apply(self.base_lp, token_out, recipient, tkn_amt_out)
        
        return amount_out

    def exchangein_basein_synthout(self, token_in, token_out, amount_in, recipient):

        lp_amt = self.base_lp.total_supply
        out = SwapDeposit().apply(self.base_lp, token_in, recipient, amount_in)
        synth_out = self.base_lp.total_supply - lp_amt
        token_out.deposit(recipient, synth_out)
        
        return synth_out


    def exchangein_synthin_baseout(self, token_in, token_out, amount_in, recipient):

        tkn_amt_out = LPQuote(False).get_amount_from_lp(self.base_lp, token_out, amount_in)
        amount_out = WithdrawSwap().apply(self.base_lp, token_out, recipient, tkn_amt_out)
        
        return int(amount_out)

    def exchangein_synthin_yieldout(self, token_in, token_out, amount_in, recipient):

        amt_out = self.exchangein_synthin_baseout(token_in, token_in.parent_tkn, amount_in, recipient)        
        self.exchangein_basein_yieldout(token_in.parent_tkn, token_out, amt_out, recipient)
        amount_yield_out = self.base_lp.last_liquidity_deposit

        return int(amount_yield_out)

    def exchangein_basein_baseout(self, token_in, token_out, amount_in, recipient):

        amount_out = Swap().apply(self.base_lp, token_in, recipient, amount_in)

        return int(amount_out)

    def exchangein_yieldin_synthout(self, token_in, token_out, amount_in, recipient):

        # Option #1: yield->base->synth
        base_out = self.exchangein_yieldin_baseout(token_in, token_out.parent_tkn, amount_in, recipient) 
        provider_amount_transfer = self.exchangein_basein_synthout(token_out.parent_tkn, token_out, base_out, recipient)

        return int(provider_amount_transfer)
                
    ## **************************** Helper Functions **************************** ##

    def remove_liquidity(self, lp, user_nm, liq):
        tokens = lp.factory.token_from_exchange[lp.name] 
        res0 = lp.get_reserve(tokens[lp.token0])
        res1 = lp.get_reserve(tokens[lp.token1])
        tot_liq = lp.get_liquidity()
        minAmount0 = SaferMath().mul_div_round(liq, res0, tot_liq)
        minAmount1 = SaferMath().mul_div_round(liq, res1, tot_liq) 
        amount0, amount1 = lp.remove_liquidity(user_nm, liq, minAmount0, minAmount1) 
        return {tokens[lp.token0].token_name: amount0, tokens[lp.token1].token_name: amount1}

    def get_reserves(self, lp, token_in):
        tokens = lp.factory.token_from_exchange[lp.name]
    
        if(token_in.token_name == lp.token0):
            x = lp.reserve0
            y = lp.reserve1
        else: 
            x = lp.reserve1
            y = lp.reserve0
    
        return (x, y)  

    def get_opp_tkn(self, lp, tkn):
        tokens = lp.factory.token_from_exchange[lp.name]
        x_tkn = tokens[[*tokens][0]]
        y_tkn = tokens[[*tokens][1]]
        
        if(tkn.token_name != x_tkn.token_name):
            return x_tkn
        elif(tkn.token_name != y_tkn.token_name):
            return x_tkn  
    
    def calc_dx(self, base_lp, token_in, dL):
    
        (x,y) = self.get_reserves(base_lp, token_in)
        L = base_lp.total_supply
    
        a = SaferMath().div_round(y, x)
        b = SaferMath().mul(2, y)
        c = -(SaferMath().exp(SaferMath().add(L, dL), 2) - SaferMath().mul(x, y))
    
        radicand = SaferMath().exp(b, 2) - 4*SaferMath().mul(a, c)
        return (-b + math.isqrt(radicand)) / (2*a)

    def update_protocol_liquidity(self, recipient, liq_amount):
        if not recipient in self.base_lp.liquidity_providers:
            self.base_lp.liquidity_providers[recipient] = {}
            self.base_lp.liquidity_providers[recipient] = liq_amount
        else:  
            self.base_lp.liquidity_providers[recipient] += liq_amount
        
    def update_mms_balance(self, account, recipient, amount):

        if not recipient in self.mm.pool.mmsBalanceOf[account]:
            self.mm.pool.mmsBalanceOf[account][recipient] = {}
            self.mm.pool.mmsBalanceOf[account][recipient] = amount
        else:
            self.mm.pool.mmsBalanceOf[account][recipient] += amount;
        
