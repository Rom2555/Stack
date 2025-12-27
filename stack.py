class Stack:
    """Реализация стека на основе списка."""

    def __init__(self):
        """Инициализирует пустой стек на основе списка."""
        self.items = []

    def is_empty(self):
        """Возвращает True, если стек пуст, иначе False."""
        return len(self.items) == 0

    def push(self, item):
        """Добавляет элемент на вершину стека."""
        self.items.append(item)

    def pop(self):
        """Удаляет и возвращает верхний элемент стека.
        Если стек пуст, выбрасывает IndexError."""
        if self.is_empty():
            raise IndexError("pop из пустого стека")
        return self.items.pop()

    def peek(self):
        """Возвращает верхний элемент стека без его удаления.
        Если стек пуст, выбрасывает IndexError."""
        if self.is_empty():
            raise IndexError("peek из пустого стека")
        return self.items[-1]

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.items)


def is_balanced(brackets):
    """Проверяет, является ли строка со скобочной последовательностью,
    сбалансированной или нет."""
    stack = Stack()
    # Словарь соответствия закрывающих и открывающих скобок
    dict_brackets = {")": "(", "}": "{", "]": "["}

    for char in brackets:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty() or stack.pop() != dict_brackets[char]:
                return False

    # Сбалансировано, если стек пустой
    return stack.is_empty()


if __name__ == "__main__":
    user_input = input("Введите последовательность скобок: ")
    result = is_balanced(user_input)
    print(f"{user_input} -> {'Сбалансированно' if result else 'Несбалансированно'}")
