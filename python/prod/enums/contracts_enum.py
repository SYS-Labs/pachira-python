from dataclasses import dataclass

@dataclass(frozen=True)
class JSONContractsEnum:
    UniswapV2Pair: str = "UniswapV2Pair"
