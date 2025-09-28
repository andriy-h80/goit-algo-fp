
# Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

# Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”.
# Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.


import matplotlib.pyplot as plt
import numpy as np


def draw_branch(x, y, length, angle, depth):
    if depth == 0:
        return

    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)
    
    plt.plot([x, x_end], [y, y_end], color='green', linewidth=depth)

    new_length = length * 0.7
    draw_branch(x_end, y_end, new_length, angle + np.pi/6, depth - 1)  # права гілка
    draw_branch(x_end, y_end, new_length, angle - np.pi/6, depth - 1)  # ліва гілка


# Налаштування вікна для малювання
plt.figure(figsize=(8, 8))
plt.axis('off')


depth = int(input("Введіть рівень рекурсії (наприклад, 5-12): ")) # можливість задати параметр глибини користувачу

draw_branch(0, 0, length=1, angle=np.pi/2, depth=depth)

plt.show()
