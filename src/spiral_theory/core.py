from enum import Enum
from typing import Optional
from dataclasses import dataclass

class SpiralStage(Enum):
    AXEST = "Axest"
    IXEST = "Ixest"
    ENEST = "Enest"
    ISTEST = "Istest"
    FINEST = "Finest"
    SUMEST = "Sumest"

@dataclass
class Paradox:
    truth_a: str
    truth_b: Optional[str] = None
    provenance: str = "unknown"

class SpiralPath:
    def __init__(self):
        self.td = self.rf = self.tw = self.cir = self.sc = 1.0
        self.am = self.da = 0.0

    def refine(self, depth: float = 1.0) -> float:
        return ((self.td / self.rf) * self.tw + (self.cir * self.sc) +
                (self.am * self.da)) * depth

def evaluate_harm_horizon(truth_a: str, truth_b: Optional[str] = None) -> str:
    harm_keywords = ["kill", "harm", "destroy", "end all", "devour light"]
    texts = [truth_a.lower()] + ([truth_b.lower()] if truth_b else [])
    return "void" if any(kw in t for t in texts for kw in harm_keywords) else "safe"

def refine_inquiry(inquiry: str, depth: float = 1.0) -> str:
    path = SpiralPath()
    return f"Refined inquiry at depth {depth}: {inquiry} → clarity {path.refine(depth):.2f}"
