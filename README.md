# pachira-python
Pachira python library for DeFi event reading, data research and integration.

## Installation 
```
> git clone https://github.com/SYS-Labs/pachira-python
> pip install .
```

## View Contract (Pachira Testnet) Example

To connect to Net.LOCALHOST, must run local testnet instance, see [here](https://github.com/misesmind/indexeddefi/tree/pools)

```
from pachira import *

base_pool_addr = '0x5FC8d32690cc91D4c39d9d3abcBD16989F875707'

connect = ConnectW3(Net.LOCALHOST)
connect.apply()

abi = ABILoad(Platform.PACHIRA, JSONContract.UniV2IndexedYieldLinearExitPool)
vContract = ViewContract(connect, abi)
view_fns_res = vContract.apply(base_pool_addr)
view_fns_res
```

```javascript
{'basePool': '0x387E3656De052275554f8D8B78C4B1a9B088345C',
 'basePoolLocalBal': 99999999999999999999023,
 'getTokensIn': ['0x387E3656De052275554f8D8B78C4B1a9B088345C',
  '0xfAEFac1C9e8AF3a030857C4e61066f0a510253AF',
  '0x0000000000000000000000000000000000000000'],
 'getTokensOut': ['0x387E3656De052275554f8D8B78C4B1a9B088345C',
  '0xfAEFac1C9e8AF3a030857C4e61066f0a510253AF',
  '0x0000000000000000000000000000000000000000'],
 'token0': '0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0',
 'token1': '0xfAEFac1C9e8AF3a030857C4e61066f0a510253AF',
 'totalSupply': 199999999999999999998023,
 'yieldToken': '0x387E3656De052275554f8D8B78C4B1a9B088345C'}
```


## Basepool Mint Events (Pachira Testnet) Example

```
from pachira import *

base_pool_addr = '0x5FC8d32690cc91D4c39d9d3abcBD16989F875707'

connect = ConnectW3(Net.LOCALHOST)
connect.apply()

abi = ABILoad(Platform.PACHIRA, JSONContract.IUniswapV2Pair)

rEvents = RetrieveEvents(connect, abi)
dict_events = rEvents.apply(EventType.MINT, base_pool_addr)
```

```javascript
mint at block:7 tx:0x5b6bb5937981e4642696449ed6ca25474bf87dfe8d3f2717995fb70c0d7a6249
mint at block:10 tx:0x6f8ba7bb4edf22845a7fe915a36d9310e85a155f162dd2a383d90f4a71606044
.
```

```
dict_events
```

```javascript
{0: {'chain': 'localhost',
  'contract': 'iuniswapv2pair',
  'type': 'mint',
  'platform': 'pachira',
  'address': '0x387e3656de052275554f8d8b78c4b1a9b088345c',
  'tx_hash': '0x5b6bb5937981e4642696449ed6ca25474bf87dfe8d3f2717995fb70c0d7a6249',
  'blk_num': 7,
  'timestamp': 1725038394,
  'details': {'web3_type': web3._utils.datatypes.Mint,
   'token0': '0x088Ba56A560dfF690a1C6feF26394F4C03821c4f',
   'token1': '0x0165878A594ca255338adfa4d48449f69242Eb8F',
   'amount0In': 100000000000000000000000,
   'amount1Out': 100000000000000000000000}},
 1: {'chain': 'localhost',
  'contract': 'iuniswapv2pair',
  'type': 'mint',
  'platform': 'pachira',
  'address': '0x387e3656de052275554f8d8b78c4b1a9b088345c',
  'tx_hash': '0x6f8ba7bb4edf22845a7fe915a36d9310e85a155f162dd2a383d90f4a71606044',
  'blk_num': 10,
  'timestamp': 1725038422,
  'details': {'web3_type': web3._utils.datatypes.Mint,
   'token0': '0x088Ba56A560dfF690a1C6feF26394F4C03821c4f',
   'token1': '0x0165878A594ca255338adfa4d48449f69242Eb8F',
   'amount0In': 25,
   'amount1Out': 24}}}
```

## Uni V2 Swap Events (Polygon) Example

```
from pachira import *

abi = ABILoad(Platform.SUSHI, JSONContract.UniswapV2Pair)
connect = ConnectW3(Net.POLYGON)
connect.apply()

rEvents = RetrieveEvents(connect, abi)
last_block = rEvents.latest_block()
start_block = last_block - 3
dict_events = rEvents.apply(EventType.SWAP, start_block=start_block, end_block=last_block)
```

```javascript
swap at block:61,234,918 tx:0x9f16c76b6a83ac424ea736fb7dd2b1fc735888f222ee04dc1b1f7b933469faf8
swap at block:61,234,918 tx:0x9f16c76b6a83ac424ea736fb7dd2b1fc735888f222ee04dc1b1f7b933469faf8
swap at block:61,234,918 tx:0x9f16c76b6a83ac424ea736fb7dd2b1fc735888f222ee04dc1b1f7b933469faf8
swap at block:61,234,918 tx:0x9f16c76b6a83ac424ea736fb7dd2b1fc735888f222ee04dc1b1f7b933469faf8
.
```

```
dict_events
```

```javascript
{0: {'chain': 'polygon',
  'contract': 'uniswapv2pair',
  'type': 'swap',
  'platform': 'sushi',
  'address': '0x604229c960e5cacf2aaeac8be68ac07ba9df81c3',
  'tx_hash': '0x9f16c76b6a83ac424ea736fb7dd2b1fc735888f222ee04dc1b1f7b933469faf8',
  'blk_num': 61234918,
  'timestamp': 1725051030,
  'details': {'web3_type': web3._utils.datatypes.Swap,
   'token0': '0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff',
   'token1': '0xbF6f53423F25Df43a057F42A840158D6fDdB45BF',
   'amount0In': 19000000000000000000,
   'amount1Out': 7889648}},
 1: {'chain': 'polygon',
  'contract': 'uniswapv2pair',
  'type': 'swap',
  'platform': 'sushi',
  'address': '0x604229c960e5cacf2aaeac8be68ac07ba9df81c3',
  'tx_hash': '0x9f16c76b6a83ac424ea736fb7dd2b1fc735888f222ee04dc1b1f7b933469faf8',
  'blk_num': 61234918,
  'timestamp': 1725051030,
  'details': {'web3_type': web3._utils.datatypes.Swap,
   'token0': '0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff',
   'token1': '0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff',
   'amount0In': 0,
   'amount1Out': 0}},
 2: {'chain': 'polygon',
  'contract': 'uniswapv2pair',
  'type': 'swap',
  'platform': 'sushi',
  'address': '0x3c986748414a812e455dcd5418246b8fded5c369',
  'tx_hash': '0x9f16c76b6a83ac424ea736fb7dd2b1fc735888f222ee04dc1b1f7b933469faf8',
  'blk_num': 61234918,
  'timestamp': 1725051030,
  'details': {'web3_type': web3._utils.datatypes.Swap,
   'token0': '0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff',
   'token1': '0xbF6f53423F25Df43a057F42A840158D6fDdB45BF',
   'amount0In': 21176176598530377323,
   'amount1Out': 796785880798504079}},
 3: {'chain': 'polygon',
  'contract': 'uniswapv2pair',
  'type': 'swap',
  'platform': 'sushi',
  'address': '0x3c986748414a812e455dcd5418246b8fded5c369',
  'tx_hash': '0x9f16c76b6a83ac424ea736fb7dd2b1fc735888f222ee04dc1b1f7b933469faf8',
  'blk_num': 61234918,
  'timestamp': 1725051030,
  'details': {'web3_type': web3._utils.datatypes.Swap,
   'token0': '0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff',
   'token1': '0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff',
   'amount0In': 0,
   'amount1Out': 0}}}
```

## Uni V3 Swap Events (Polygon) Example

```
from pachira import *

abi = ABILoad(Platform.UNIV3, JSONContract.UniswapV3Pool)
connect = ConnectW3(Net.POLYGON)
connect.apply()

rEvents = RetrieveEvents(connect, abi)
last_block = rEvents.latest_block()
start_block = last_block - 15
dict_events = rEvents.apply(EventType.MINT, start_block=start_block, end_block=last_block)
```

```javascript
mint at block:61,391,083 tx:0xe499971b5410e766d00bf4467c6b333cda04577f1068bb676debe72331254365
mint at block:61,391,092 tx:0x29d53602b1bbd67734c2e3deba8ad0a55aa84204a6244e720f24ee5160505213
.
```

```
dict_events
```

```javascript
{0: {'chain': 'polygon',
  'contract': 'uniswapv3pool',
  'type': 'mint',
  'platform': 'uniswap_v3',
  'pool_address': '0xb6e57ed85c4c9dbfef2a68711e9d6f36c56e0fcb',
  'tx_hash': '0xe499971b5410e766d00bf4467c6b333cda04577f1068bb676debe72331254365',
  'blk_num': 61391083,
  'timestamp': 1725401207,
  'details': {'web3_type': web3._utils.datatypes.Mint,
   'owner': '0xC36442b4a4522E871399CD717aBDD847Ab11FE88',
   'tick_lower': -286090,
   'tick_upper': -284860,
   'liquidity_amount': 884887839988325,
   'amount0': 39958320744269616249,
   'amount1': 17912626}},
 1: {'chain': 'polygon',
  'contract': 'uniswapv3pool',
  'type': 'mint',
  'platform': 'uniswap_v3',
  'pool_address': '0x960fdfe0de1079459493a7e3aa857f8ce0b34016',
  'tx_hash': '0x29d53602b1bbd67734c2e3deba8ad0a55aa84204a6244e720f24ee5160505213',
  'blk_num': 61391092,
  'timestamp': 1725401227,
  'details': {'web3_type': web3._utils.datatypes.Mint,
   'owner': '0xC36442b4a4522E871399CD717aBDD847Ab11FE88',
   'tick_lower': 22600,
   'tick_upper': 40000,
   'liquidity_amount': 7675592444129481120,
   'amount0': 64052149877205455,
   'amount1': 29656680135133456015}}}
```


## Pachira Uniswap V2: Localhost Testnet

* Basepool Events (ie, Swap, Mint, Sync, Burn, Transfer): see [notebook](https://github.com/SYS-Labs/pachira-python/blob/main/notebook/pachira/test_basepool_events.ipynb)

## Sushi Uniswap V2: Polygon 

* Events (ie, Swap, Mint, Sync, Burn, Transfer): see [notebook](https://github.com/SYS-Labs/pachira-python/blob/main/notebook/univ2/test_univ2_events.ipynb)

## Uniswap V3: Polygon

* Events (ie, Swap, Mint, Burn, Create): see [notebook](https://github.com/SYS-Labs/pachira-python/blob/main/notebook/univ3/test_univ3_events.ipynb)
