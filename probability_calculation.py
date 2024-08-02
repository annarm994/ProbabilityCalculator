from collections import Counter

def calculate_probability_distribution(rolls, M, N):
    """Calculate the probability distribution of sums from the rolls."""
    max_sum = M * N
    min_sum = M
    count = Counter(rolls)
    total_rolls = len(rolls)
    distribution = {i: count[i] / total_rolls for i in range(min_sum, max_sum + 1)}
    return distribution
