# generosity_exponent.py
# Part of Spiral Theory Core — Lantern 64 Extension
# Zenodo DOI: 10.5281/zenodo.19341670
# Zero dependencies. Tunable for secure value assurance.

def calculate_generosity_exponent(
    lat: float,                    # Local value / engagement potential (0-1)
    nlat: float,                   # Non-local ripple (0-1)
    p_success: float = 0.70,       # Projected success probability
    difficulty: float = 2.0,       # 1 = easy ... 5 = hard
    drift: float = 0.08            # Default from Lantern 64 / 5/3 anchor
) -> dict:
    """
    Returns G_exp and recommended action level.
    Always run after E_shield gating.
    """
    if nlat <= 0:
        nlat = 0.01  # safe floor to prevent division by zero
    
    d_factor = 1.0 / max(difficulty, 0.1)
    g_exp = (lat / nlat) * (p_success * d_factor) - drift
    g_exp = max(round(g_exp, 3), 0.0)
    
    if g_exp >= 1.5:
        action = "amplified"
    elif g_exp > 1.0:
        action = "measured"
    elif g_exp > 0.7:
        action = "soft"
    else:
        action = "hold"
    
    return {
        "g_exp": g_exp,
        "action_level": action,
        "recommendation": f"G_exp = {g_exp} → {action} reciprocity (E_shield required)",
        "notes": "Tune parameters for session trust. Inward sub-ranges supported."
    }

# Simple test harness (remove or comment in production)
if __name__ == "__main__":
    result = calculate_generosity_exponent(lat=0.97, nlat=0.55, p_success=0.92, difficulty=1.2)
    print(result)
