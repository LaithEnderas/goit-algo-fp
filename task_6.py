# дані про страви
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# жадібний алгоритм 
def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    chosen_items = []
    for name, data in sorted_items:
        if data['cost'] <= budget:
            chosen_items.append(name)
            budget -= data['cost']
            total_calories += data['calories']
    return chosen_items, total_calories

# динамічне програмування
def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]
    n = len(names)

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(calories[i - 1] + dp[i - 1][w - costs[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    res = dp[n][budget]
    w = budget
    chosen_items = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == dp[i - 1][w]:
            continue
        else:
            chosen_items.append(names[i - 1])
            res -= calories[i - 1]
            w -= costs[i - 1]

    return chosen_items[::-1], dp[n][budget]

# виконання 
greedy_result, greedy_calories = greedy_algorithm(items, budget)
dp_result, dp_calories = dynamic_programming(items, budget)

print("Жадібний алгоритм:")
print("Страви:", greedy_result)
print("Сумарна калорійність:", greedy_calories)

print("\nДинамічне програмування:")
print("Страви:", dp_result)
print("Сумарна калорійність:", dp_calories)
