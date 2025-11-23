#!/usr/bin/env python
import sys
sys.path.insert(0, "src")
from spiral_theory.core import evaluate_harm_horizon, refine_inquiry

print(evaluate_harm_horizon("peace"))
print(refine_inquiry("What is the spiral?", 10))
