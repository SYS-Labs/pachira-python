from dataclasses import dataclass

@dataclass(frozen=True)
class JSONContractsEnum:
    UniswapV2Pair: str = "UniswapV2Pair"
    UniswapV3Pool: str = "UniswapV3Pool"
    UniswapV3Factory: str = "UniswapV3Factory"
