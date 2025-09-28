
# Завдання 6. Жадібні алгоритми та динамічне програмування

# Необхідно написати програму на Python, яка використовує два підходи — # жадібний алгоритм та алгоритм динамічного програмування
# для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.
# Кожен вид їжі має вказану вартість і калорійність. (Страву можна брати 1 раз).
# Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.

# Розробіть функцію greedy_algorithm жадібного алгоритму,
# яка вибирає страви, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.
# Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming,
# яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    for item, details in sorted_items:
        if details['cost'] <= remaining_budget:
            chosen_items.append(item)
            total_calories += details['calories']
            remaining_budget -= details['cost']
        
    return total_calories, budget - remaining_budget, chosen_items


def dynamic_programming(items, budget):
    item_names = list(items.keys())

    dp_table = [[0 for x in range(budget + 1)] for y in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        cost = items[item_names[i-1]]['cost']
        calories = items[item_names[i-1]]['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp_table[i][w] = max(dp_table[i-1][w], dp_table[i-1][w - cost] + calories)
            else:
                dp_table[i][w] = dp_table[i-1][w]

    chosen_items = []
    temp_budget = budget

    for i in range(len(items), 0, -1):
        if dp_table[i][temp_budget] != dp_table[i-1][temp_budget]:
            chosen_items.append(item_names[i-1])
            temp_budget -= items[item_names[i-1]]['cost']

    chosen_items.reverse()

    return dp_table[len(items)][budget], budget - temp_budget, chosen_items


if __name__ == '__main__':
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print('Найбільша сумарна калорійність згідно жадібного алгоритму:', greedy_result)
    print('Найбільша сумарна калорійність згідно алгоритму динамічного програмування:', dp_result)
