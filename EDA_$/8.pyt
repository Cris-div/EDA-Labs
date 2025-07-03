test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top    = None
        self._size = 0

    def push(self, data):
        """Push element using linked nodes."""
        # Your solution here 🛠️
        node=Node(data)
        node.next=self.top
        self.top=node
        self._size+=1



    def pop(self):
        """Pop and return top data or None."""
        # Your solution here 🛠️
        if not self.top:
            return None
        data=self.top.data
        self.top=self.top.next
        self._size-=1
        return data

        


    def peek(self):
        """Return top data without removing or None."""
        # Your solution here 🛠️
        return self.top.data if self.top else None

    def size(self):
        """Return number of items."""
        # Your solution here 🛠️
        return self._size 

def test_o4_2():
    stack = LinkedStack()
    cond_empty = stack.peek() is None and stack.pop() is None and stack.size() == 0
    record_test("o4.2.1 empty behavior", cond_empty)

    stack.push(5)
    stack.push(7)
    stack.push(9)
    cond_push = stack.peek() == 9 and stack.size() == 3
    record_test("o4.2.2 push/peek/size", cond_push)

    stack.pop()
    cond_after_pop = stack.peek() == 7 and stack.size() == 2
    record_test("o4.2.3 pop adjusts", cond_after_pop)

    stack.push("a")
    cond_mixed = stack.peek() == "a" and stack.size() == 3
    record_test("o4.2.4 mixed types", cond_mixed)

    cond_types = isinstance(stack.peek(), (int, str, type(None))) and isinstance(stack.size(), int)
    record_test("o4.2.5 return-type verification", cond_types)

# 🚀 Run tests
test_o4_2()

# 📋 Summary
for result in test_results:
    print(result)