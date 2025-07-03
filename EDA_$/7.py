test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Return True if stack is empty."""
        # Your solution here 🛠️
        return len(self.items)==0

    def push(self, data):
        """Push data onto the stack."""
        # Your solution here 🛠️
        return self.items.append(data)

    def pop(self):
        """Pop and return top item or None if empty."""
        # Your solution here 🛠️
        return self.items.pop() if self.items else None

def test_o4_1():
    main_stack = Stack()
    cond_core = (
        main_stack.is_empty() is True
        and main_stack.push(1) is None
        and main_stack.push(2) is None
        and main_stack.items == [1, 2]
        and main_stack.pop() == 2
        and main_stack.pop() == 1
    )
    record_test("o4.1.1 core operations", cond_core)

    secondary_stack = Stack()
    record_test("o4.1.2 pop on empty", secondary_stack.pop() is None)

    mixed_stack = Stack()
    mixed_stack.push(0)
    mixed_stack.push(99)
    cond_mixed = mixed_stack.pop() == 99 and mixed_stack.is_empty() is False
    record_test("o4.1.3 mixed operations", cond_mixed)

    any_stack = Stack()
    any_stack.push(None)
    any_stack.push("x")
    record_test("o4.1.4 input-agnostic storage", any_stack.items == [None, "x"])

    popped_value = main_stack.pop()
    cond_types = isinstance(main_stack.is_empty(), bool) and isinstance(
        popped_value, (int, str, type(None))
    )
    record_test("o4.1.5 return-type verification", cond_types)

# 🚀 Run tests
test_o4_1()

# 📋 Summary
for result in test_results:
    print(result)