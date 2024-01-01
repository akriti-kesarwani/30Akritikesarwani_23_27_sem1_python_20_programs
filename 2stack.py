class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop from an empty stack.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. Cannot peek at an empty stack.")

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Current stack:", stack.items)
print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("After popping, current stack:", stack.items)
print("Stack size:", stack.size())
