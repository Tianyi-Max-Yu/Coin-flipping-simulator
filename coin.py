import random

def flip_coin():
    """Simulates flipping a coin."""
    return "Heads" if random.choice([True, False]) else "Tails"

def coin_flip_simulator():
    """Runs the coin flipping simulator."""
    print("Welcome to the Coin Flipping Simulator!")
    while True:
        flips = input("Enter the number of flips you want to simulate (or 'q' to quit): ")
        if flips.lower() == 'q':
            print("Thanks for using the Coin Flipping Simulator. Goodbye!")
            break
        elif flips.isdigit() and int(flips) > 0:
            flips = int(flips)
            results = {"Heads": 0, "Tails": 0}
            for _ in range(flips):
                result = flip_coin()
                results[result] += 1
            print(f"Results: {results['Heads']} Heads and {results['Tails']} Tails")
        else:
            print("Please enter a valid positive number or 'q' to quit.")

if __name__ == "__main__":
    coin_flip_simulator()
