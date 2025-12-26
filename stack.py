class Stack:
    def __init__(self):
        """Инициализирует пустой стек на основе списка."""
        self.items = []

    def is_empty(self):
        """Возвращает True, если стек пуст, иначе False."""
        if not self.items:
            return True
        else:
            return False

    def push(self, item):
        """Добавляет элемент на вершину стека."""
        self.items.append(item)

    def pop(self):
        """Удаляет и возвращает верхний элемент стека. Если стек пуст, поведение не определено."""
        self.items.pop()
        return self.items[-1] if not self.is_empty() else print('Стек пуст')

    def peek(self):
        """Возвращает верхний элемент стека без его удаления. Если стек пуст, выдает "Стек пуст"."""
        return self.items[-1] if not self.is_empty() else print('Стек пуст')

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    user_input = input('Введите строку: ')
    for i in user_input:
        s.push(i)
    print(s.size())
    print(s.is_empty())


