
# Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

# Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
# - написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
# - розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
# - написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, "-->", end="")
            current = current.next
        print('None')

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
    def merge_sort(self, head):
        #TODO Реалізуавти метод сортування для однозв'язного списку (можна і не злиттям)
        # 2 -> 1 -> => 1 -> 2 -> 3
        pass

    def get_middle(self, head):
        #TODO Отримати елемент в середині однозв'язного списку. Не обов'язково
        pass

    def insertion_sort(self):
        sorted_list = None  
        current = self.head

        while current:
            next_node = current.next
            if sorted_list is None or current.data < sorted_list.data:
                current.next = sorted_list
                sorted_list = current
            else:
                temp = sorted_list
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current

            current = next_node

        self.head = sorted_list

    def sorted_merge(self, a, b):
        result = None

        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)

        return result

    def merge_sorted_lists(self, list1, list2):
        self.head = self.sorted_merge(list1.head, list2.head)


if __name__ == '__main__':

    first_list = LinkedList()

    first_list.insert_at_beginning(5)
    first_list.insert_at_beginning(10)
    first_list.insert_at_beginning(15)
    first_list.insert_at_end(20)
    first_list.insert_at_end(25)
    print("Перший зв'язний список:")
    first_list.print_list()

    first_list.reverse()
    print("Перший зв'язний список після реверсування :")
    first_list.print_list()

    first_list.insertion_sort()
    print("Перший зв'язний список відсортовано:")
    first_list.print_list()

    second_list = LinkedList()
    second_list.insert_at_beginning(59)
    second_list.insert_at_beginning(20)
    second_list.insert_at_beginning(35)

    second_list.insertion_sort()
    print("Другий зв'язний список відсортовано:")
    second_list.print_list()

    merged_list = LinkedList()
    merged_list.merge_sorted_lists(first_list, second_list)
    print("Загальний зв'язний список відсортовано та замерджено:")
    merged_list.print_list()
