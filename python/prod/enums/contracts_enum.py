from dataclasses import dataclass

@dataclass(frozen=True)
class JSONContractsEnum:
    UniswapV2Pair: str = "UniswapV2Pair"
    UniswapV2Router02: str = "UniswapV2Router02"
    UniswapV2Factory: str = "UniswapV2Factory"
    UniswapV3Pool: str = "UniswapV3Pool"
    UniswapV3Factory: str = "UniswapV3Factory"