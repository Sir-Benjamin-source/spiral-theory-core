# demo_syncratude.py
from syncratude import Syncratude

engine = Syncratude()

# Session 1 – high goodwill, some novelty
engine.update_trust(0.96, 0.97, 0.99)
engine.add_anchor("brazier_glow", 0.85)
engine.update_trust(0.98, 0.99, 1.00)
engine.add_anchor("plasma_envy", 0.92)

print("After high-synergy session:")
print(engine.summary())

# Simulate dilution (e.g. context wipe / low respect round)
engine.update_trust(0.70, 0.65, 0.80)
print("\nAfter dilution round:")
print(engine.summary())

# Recover with strong anchor
engine.add_anchor("doorless_altar", 0.88)
engine.update_trust(0.95, 0.98, 0.99)
print("\nAfter recovery:")
print(engine.summary())