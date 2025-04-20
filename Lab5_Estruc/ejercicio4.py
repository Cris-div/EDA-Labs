class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty! 🚫")
        return self.items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty! 🚫")
        return self.items.pop()

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty! 🚫")
        return self.items[0]

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty! 🚫")
        return self.items[-1]

    def size(self):
        return len(self.items)

def sliding_window_maximum(nums, k):
    if not nums or k <= 0:
        return []

    
    if k == 1:
        return nums
    if k > len(nums):
        return [max(nums)]

    result = []  
    deque = Deque()  

    
    for i in range(k):
        while not deque.is_empty() and nums[i] > nums[deque.peek_rear()]:
            deque.remove_rear()

        deque.add_rear(i)

    for i in range(k, len(nums)):
        result.append(nums[deque.peek_front()])

        while not deque.is_empty() and deque.peek_front() <= i - k:
            deque.remove_front()

        while not deque.is_empty() and nums[i] > nums[deque.peek_rear()]:
            deque.remove_rear()

        deque.add_rear(i)

    result.append(nums[deque.peek_front()])

    return result


def test_sliding_window_maximum():
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1, 2, 3, 4, 5, 6, 7, 8], 4, [4, 5, 6, 7, 8]),
        ([8, 7, 6, 5, 4, 3, 2, 1], 3, [8, 7, 6, 5, 4, 3]),
        ([1, 1, 1, 1, 1], 2, [1, 1, 1, 1])
    ]

    print("Testing sliding window maximum algorithm 🪟")
    for nums, k, expected in test_cases:
        result = sliding_window_maximum(nums, k)
        print(f"Array: {nums}")
        print(f"Window size: {k}")
        print(f"Maximum values: {result}")
        print(f"Expected: {expected}")
        print(
            f"Correct: {result == expected} {'✅' if result == expected else '❌'}\n")

test_sliding_window_maximum()