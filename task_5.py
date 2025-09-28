
# Завдання 5. Візуалізація обходу бінарного дерева

# Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python,
# яка візуалізує обходи дерева: у глибину та в ширину.
# Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0).
# Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу.
# Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.
#  👉🏻 Примітка. Використовуйте стек та чергу, НЕ рекурсію


from collections import deque
import heapq
import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = [colors.get(node, 'skyblue') for node in tree.nodes()]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()


def build_heap_tree(heap, index=0):
    if index >= len(heap):
        return None

    root = Node(heap[index])

    left_index = 2 * index + 1
    right_index = 2 * index + 2

    root.left = build_heap_tree(heap, left_index)
    root.right = build_heap_tree(heap, right_index)

    return root


def generate_color(step, total_steps):
    base_color = [0, 0, 255]
    darken_factor = step / total_steps
    new_color = [
        int(base_color[i] + (255 - base_color[i]) * darken_factor)
        for i in range(3)
    ]
    return f'#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}'


def dfs_visualize(root, total_steps):
    visited = set()
    stack = [root]
    colors = {}
    step = 0

    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            visited.add(node.id)
            color = generate_color(step, total_steps)
            node.color = color
            colors[node.id] = color
            step += 1

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return colors


def bfs_visualize(root, total_steps):
    visited, queue = set(), deque([root])
    colors = {}
    step = 0

    while queue:
        node = queue.popleft()
        if node and node.id not in visited:
            visited.add(node.id)
            color = generate_color(step, total_steps)
            node.color = color
            colors[node.id] = color
            step += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return colors


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


if __name__ == '__main__':
    heap_list = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
    heapq.heapify(heap_list)
    # Побудова дерева з купи
    heap_tree_root = build_heap_tree(heap_list)

    # Обрахунок кількості кроків (вузлів)
    total_steps = count_nodes(heap_tree_root)

    # DFS візуалізація
    dfs_colors = dfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, dfs_colors)

    # BFS візуалізація
    heap_tree_root = build_heap_tree(heap_list)  # Побудова дерева з купи (повторна)
    bfs_colors = bfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, bfs_colors)
