import random
import matplotlib.pyplot as plt
from collections import Counter

def monte_carlo_dice_simulation(num_rolls=100000):
    sums = []
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sums.append(die1 + die2)

    counts = Counter(sums)
    probabilities = {s: count / num_rolls for s, count in counts.items()}
    return probabilities

# виконуємо симуляцію
num_rolls = 100000
probabilities = monte_carlo_dice_simulation(num_rolls)

# виведення таблиці
print("Сума\tЙмовірність (%)")
for s in sorted(probabilities):
    print(f"{s}\t{probabilities[s]*100:.2f}%")

# побудова графіка
plt.figure(figsize=(10, 6))
plt.bar(probabilities.keys(), [p * 100 for p in probabilities.values()], color='skyblue')
plt.title(f"Ймовірність сум при киданні двох кубиків ({num_rolls} кидків)")
plt.xlabel("Сума")
plt.ylabel("Ймовірність (%)")
plt.xticks(range(2, 13))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
