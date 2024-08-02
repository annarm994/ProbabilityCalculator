import random

def roll_dice(M, N):
    """Simulate rolling M N-sided dice once and return the sum of outcomes."""
    return sum(random.randint(1, N) for _ in range(M))

def simulate_rolls(M, N, K):
    """Simulate rolling M N-sided dice K times and return a list of sums."""
    return [roll_dice(M, N) for _ in range(K)]
