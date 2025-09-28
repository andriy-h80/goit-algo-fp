
# Завдання 7. Використання методу Монте-Карло

# Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел,
# які випадають на кубиках, і визначає ймовірність кожної можливої суми.
# Створіть симуляцію, де два кубики кидаються велику кількість разів.
# Для кожного кидка визначте суму чисел, які випали на обох кубиках.
# Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції.
# Використовуючи ці дані, обчисліть імовірність кожної суми.

# На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

# Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.
#     Сума	   Імовірність
# 2	  2.78%    (1/36)
# 3	  5.56%    (2/36)
# 4	  8.33%    (3/36)
# 5	  11.11%   (4/36)
# 6	  13.89%   (5/36)
# 7	  16.67%   (6/36)
# 8	  13.89%   (5/36)
# 9	  11.11%   (4/36)
# 10  8.33%    (3/36)
# 11  5.56%    (2/36)
# 12  2.78%    (1/36)

# Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці вище.


import random
import matplotlib.pyplot as plt

analytical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

def simulate_dice_rolls(num_rolls):
    counts = {s: 0 for s in range(2, 13)}
    
    # Симуляція кидків
    for _ in range(num_rolls):
        dice = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        counts[dice + dice_two] += 1
    
    probabilities = {s: counts[s] / num_rolls for s in counts}
    
    return probabilities


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    # Створення графіка
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках')
    
    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')
    
    plt.show()


if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        print(f"\n===== Симуляція {accuracy} кидків =====")
        # Симуляція кидків і обчислення ймовірностей
        probabilities = simulate_dice_rolls(accuracy)

        # Відображення ймовірностей на графіку
        plot_probabilities(probabilities)

        print("Сума | Монте-Карло | Аналітика | Відхилення")
        print("-----|------------ |-----------|-----------")
        for s in range(2, 13):
            mc_prob = probabilities[s]
            analit_prob = analytical_probabilities[s]
            diff = mc_prob - analit_prob
            print(f"{s:>4} | {mc_prob:11.2%} | {analit_prob:9.2%} | {diff:9.2%} ")
