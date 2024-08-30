# pachira-python
Pachira python library for DeFi event reading, data research and integration.

## Installation 
```
> git clone https://github.com/SYS-Labs/pachira-python
> pip install .
```

or 

```
> pip install pachira-python
```

## Implementation: View Contract

```
from pachira import *

base_pool_addr = '0x5FC8d32690cc91D4c39d9d3abcBD16989F875707'

connect = ConnectW3(Net.LOCALHOST)
connect.apply()

abi = ABILoading(Platform.PACHIRA, JSONContract.UniV2IndexedYieldLinearExitPool)
vContract = ViewContract(connect, abi)
view_fns_res = vContract.apply(index_pool_addr)
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

## Implementation: Swap Events

```
from pachira import *

abi = ABILoading(Platform.SUSHI, JSONContract.UniswapV2Pair)
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


## Pachira Uniswap V2: Localhost Testnet

* Basepool Events: see [notebook](https://github.com/SYS-Labs/pachira-python/blob/main/notebook/pachira/test_basepool_events.ipynb)

## Sushi Uniswap V2: Polygon 

* Events: see [notebook](https://github.com/SYS-Labs/pachira-python/blob/main/notebook/pachira/test_univ2_events.ipynb)

## Uniswap V3: Polygon

* Swap: see [notebook](https://github.com/SYS-Labs/pachira-python/blob/main/notebook/univ3/swap.ipynb)
* Mint: see [notebook](https://github.com/SYS-Labs/pachira-python/blob/main/notebook/univ3/mint.ipynb)
* Burn: see [notebook](https://github.com/SYS-Labs/pachira-python/blob/main/notebook/univ3/burn.ipynb)
* Pool Creation: see [notebook](https://github.com/SYS-Labs/pachira-python/blob/main/notebook/univ3/pool_created.ipynb) 