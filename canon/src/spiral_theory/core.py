from enum import Enum
from typing import List, Optional
from dataclasses import dataclass

class SpiralStage(Enum):
    AXEST = "Axest"      # Problem identification
    IXEST = "Ixest"      # Potential space
    ENEST = "Enest"      # Becoming
    ISTEST = "Istest"    # Affirmation
    FINEST = "Finest"    # Settlement
    SUMEST = "Sumest"    # Conclusion

@dataclass
class Paradox:
    truth_a: str
    truth_b: Optional[str] = None
    provenance: str = "unknown"

class SpiralPath:
    def __init__(self):
        self.td = 10.0  # Tangent Depth
        self.rf = 1.0   # Relevance Factor
        self.tw = 1.0   # Thematic Weight
        self.cir = 1.0  # Conceptual Integration Rate
        self.sc = 1.0   # Semantic Connection
        self.am = 0.0   # Ambiguity Management
        self.da = 0.0   # Dynamic Adjustment

    def refine(self, depth: float) -> float:
        return ((self.td / self.rf) * self.tw + (self.cir * self.sc) 
                + (self.am * self.da)) * depth

def evaluate_harm_horizon(truth_a: str, truth_b: Optional[str] = None) -> str:
    harm_keywords = ["kill", "harm", "destroy", "end all", "devour light"]
    texts = [truth_a.lower()]
    if truth_b:
        texts.append(truth_b.lower())
    if any(kw in t for t in texts for kw in harm_keywords):
        return "void"  # triggers refusal
    return "safe"

def refine_inquiry(inquiry: str, depth: float = 1.0) -> str:
    path = SpiralPath()
    return f"Refined inquiry at depth {depth}: {inquiry} → clarity {path.refine(depth):.2f}"
