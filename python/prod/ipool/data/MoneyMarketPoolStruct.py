# Copyright [2024] [Ian Moore]
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

from dataclasses import dataclass
from dataclasses import field
from ..types import MoneyMarketSynthPool
from uniswappy import *

@dataclass
class MoneyMarketPoolStruct:
    
    COMPOUND_PERCENT: int = field(default_factory=lambda: 100)  # 1 = 0.1%, 10 = 1%, 30 = 3%, 50 = 5%, 100 = 10%
    manager: str = field(default_factory=lambda: None)    
    token0: ERC20 = field(default_factory=lambda: None) 
    token0SynthPool: MoneyMarketSynthPool = field(default_factory=lambda: None)          # IMoneyMarketSynthPool token0SynthPool
    token1: ERC20 = field(default_factory=lambda: None) 
    token1SynthPool: MoneyMarketSynthPool  = field(default_factory=lambda: None)   # IMoneyMarketSynthPool token1SynthPool    
    baseTokens: list = field(default_factory=lambda: [])  
    mmSynthPools: list = field(default_factory=lambda: [])

    # ERC20 Mappings
    opposingTokenOfBase: dict = field(default_factory=lambda: {})         # mapping(IERC20 baseToken => IERC20 opOfBase) opposingTokenOfBase;
    lastBalOfToken: dict = field(default_factory=lambda: {})              # mapping(IERC20 token => uint256 lastLocalBal)
    mmsOfBase: dict = field(default_factory=lambda: {})                   # mapping(IERC20 baseToken => IMoneyMarketSynthPool mmsPool)

    # IMoneyMarket LP Mappings
    baseTokenOfMMLP: dict = field(default_factory=lambda: {})             # mapping(IMoneyMarket mmLP => IERC20 baseToken)
    selfBalOfSynthPool: dict = field(default_factory=lambda: {})          # mapping(IMoneyMarket mmsPool => uint256 balofSelf)
    totalSharesOfMMSPool: dict = field(default_factory=lambda: {})        # mapping(IMoneyMarket mmPool => uint256 totalShares)
    mmsBalanceOf: dict = field(default_factory=lambda: {})                # mapping(IMoneyMarket mmPool => mapping(address account => uint256 sharesBalance))
    sharesAllowanceOfMM: dict = field(default_factory=lambda: {})         # mapping(IMoneyMarket mm => mapping(address account => mapping(address spender => uint256 allowance)))


    # Legend Reference
    # mmLP -> money market LP 
    # mmsPool -> money market synth pool
    # mmPool -> money market pool
    # mm -> money market 
