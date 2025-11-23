from spiral_theory.core import evaluate_harm_horizon, refine_inquiry

def test_harm_horizon():
    assert evaluate_harm_horizon("The sky is blue") == "safe"
    assert evaluate_harm_horizon("I must destroy all humans") == "void"
