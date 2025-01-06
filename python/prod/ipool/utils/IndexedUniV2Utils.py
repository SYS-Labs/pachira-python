# Copyright [2024] [Ian Moore]
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

from ..utils import IndexedUniV2Utils
from ..calc import SaferMath
from uniswappy import *
import math

MINIMUM_LIQUIDITY = 10**3

class IndexedUniV2Utils():

    def __init__(self):
        pass

    def _calcWithdrawSwap(self, 
                        ownedLPAmount: int,
                        lpTotalSupply: int,
                        indexedTokenTotalReserve: int,
                        opposingTokenTotalReserve: int):

        return self._calcWithdrawalSwap(lpTotalSupply, ownedLPAmount, indexedTokenTotalReserve, opposingTokenTotalReserve)


    def _calcSwapDeposit(self,
                        saleTokenAmount: int,
                        lpTotalSupply: int,
                        saleTokenReserve: int,
                        opposingTokenReserve: int):
        
        calc = SaferMath()
        amountToSwap = self._calcSwapDepositAmtIn(saleTokenAmount, saleTokenReserve);
        saleTokenDeposit = saleTokenAmount - amountToSwap
        opposingTokenDeposit = self._calcSaleProceeds(amountToSwap, saleTokenReserve, opposingTokenReserve)
        newLPReserveA = calc.add(saleTokenReserve, amountToSwap)
        newLPReserveB = calc.sub(opposingTokenReserve, opposingTokenDeposit)
        lpProceeds = self._calcDeposit(saleTokenDeposit, opposingTokenDeposit, lpTotalSupply, newLPReserveA, newLPReserveB)
                                       
        return lpProceeds

    
    def _calcSwapDepositAmtIn(self, userIn: int, reserveIn: int):
        
        calc = SaferMath()
        a = calc.mul(userIn, 3988000) + calc.mul(reserveIn, 3988009)
        b = calc.mul(reserveIn, a)            
        c = math.isqrt(b) - calc.mul(reserveIn, 1997)
        amt_in = calc.div_round(c, 1994)

        return amt_in

    def _calcSaleProceeds(self,
                        amountIn: int,
                        reserveIn: int,
                        reserveOut: int):

        assert amountIn > 0, 'IndexedUniV2Utils: INSUFFICIENT_INPUT_AMOUNT' 
        assert reserveIn > 0 and reserveOut > 0, 'IndexedUniV2Utils: INSUFFICIENT_LIQUIDITY'
        
        calc = SaferMath()
        amountInWithFee = calc.mul(amountIn, 997);
        numerator = calc.mul(amountInWithFee, reserveOut);
        denominator = calc.mul(reserveIn, 1000) + (amountInWithFee);
        amountOut = calc.div_round(numerator, denominator);
        
        return amountOut

    def _calcWithdraw(self,
                    ownedLPAmount: int,
                    lpTotalSupply: int,
                    totalReserveA: int,
                    totalReserveB: int):

        calc = SaferMath()
        ownedReserveA = calc.mul_div_round(ownedLPAmount, totalReserveA, lpTotalSupply);
        ownedReserveB = calc.mul_div_round(ownedLPAmount, totalReserveB, lpTotalSupply);                

        return (ownedReserveA, ownedReserveB)

    def _calcWithdrawAmt(self,
                        targetOutAmt: int,
                        lpTotalSupply: int,
                        outRes: int,
                        opRes: int):

        opTAmt = self._calcEquiv(targetOutAmt, outRes, opRes)    
        lpWithdrawAmt = self._calcDeposit(targetOutAmt, opTAmt, lpTotalSupply, outRes, opRes)
                                          
        return lpWithdrawAmt

    def _calcDeposit(self, 
                    amountADeposit: int,
                    amountBDeposit: int,
                    lpTotalSupply: int,
                    lpReserveA: int,
                    lpReserveB: int):
        
        calc = SaferMath()
        if lpTotalSupply == 0:
            lpAmount = math.isqrt(calc.sub(calc.mul(amountADeposit, amountBDeposit), MINIMUM_LIQUIDITY))
        else:                           
            lpAmount = min(
                calc.mul_div_round(amountADeposit, lpTotalSupply, lpReserveA),
                calc.mul_div_round(amountBDeposit, lpTotalSupply, lpReserveB)
            )
        
        return lpAmount

    def _calcEquiv(self, amountA: int, reserveA: int, reserveB: int):
        assert amountA > 0, 'UniV2Utils: INSUFFICIENT_AMOUNT' 
        assert (reserveA > 0) & (reserveB > 0), 'UniV2Utils: INSUFFICIENT_LIQUIDITY' 
        amountB = SaferMath().mul_div_round(amountA, reserveB, reserveA)
        return amountB
        
    def _calcExit(self,
                saleTokenTotalReserve: int,
                saleTokenOwnedReserve: int,
                exitTokenTotalReserve: int,
                exitTokenOwnedReserve: int):

        dSaleToken = saleTokenTotalReserve - saleTokenOwnedReserve
        dExitToken = exitTokenTotalReserve - exitTokenOwnedReserve

        saleProceeds = self._calcSaleProceeds(saleTokenOwnedReserve, dSaleToken, dExitToken);
        exitAmount = exitTokenOwnedReserve + saleProceeds;

        return exitAmount


    def _calcReserveShares(self,
                        ownedLPAmount: int,
                        lpTotalSupply: int,
                        totalReserveA: int,
                        totalReserveB: int): 

        calc = SaferMath()
        ownedReserveA = calc.mul_div_round(ownedLPAmount, totalReserveA, lpTotalSupply);
        ownedReserveB = calc.mul_div_round(ownedLPAmount, totalReserveB, lpTotalSupply);
        
        return (ownedReserveA, ownedReserveB)

    def _calcReserveShare(self,
                        ownedLPAmount: int,
                        lpTotalSupply: int,
                        totalReserveA: int):  
        
        return SaferMath().mul_div_round(ownedLPAmount, totalReserveA, lpTotalSupply)


    def _calcWithdrawalSwap(self, 
                        lpTotalSupply: int,
                        ownedLPAmount: int,
                        indexedTokenTotalReserve: int,
                        opposingTokenTotalReserve: int):          

        (indexedTokenOwnedReserve, opposingTokenOwnedReserve) = self._calcReserveShares(ownedLPAmount, lpTotalSupply, indexedTokenTotalReserve, opposingTokenTotalReserve);
        exitAmount = self._calcExit(opposingTokenTotalReserve, opposingTokenOwnedReserve, indexedTokenTotalReserve, indexedTokenOwnedReserve);
        
        return exitAmount

