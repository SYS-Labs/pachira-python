from dataclasses import dataclass

@dataclass(frozen=True)
class PlatformsEnum:
    SUSHI: str = "sushi"
    PACHIRA: str = "pachira"
