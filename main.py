from dice_simulation import simulate_rolls
from probability_calculation import calculate_probability_distribution

def main():
    N = int(input("Enter the number of sides on the dice (N): "))
    M = int(input("Enter the number of dice to roll (M): "))
    K = int(input("Enter the number of times to roll the dice (K): "))
    
    rolls = simulate_rolls(M, N, K)
    
    distribution = calculate_probability_distribution(rolls, M, N)
    
    print("\nProbability Distribution:")
    for sum_value, probability in sorted(distribution.items()):
        print(f"Sum {sum_value}: {probability:.4f}")

if __name__ == "__main__":
    main()
