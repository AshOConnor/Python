from collections import deque
queue = deque(["Ash", "Gemma", "Lockie", "Elvis", "Romeo"])
queue.append("John")
queue.append("Mary")
queue.popleft()
queue.popleft()
stack = [5]
stack.append("Liam")
stack.pop()
queue.popleft()
queue.popleft()
queue.popleft()
queue.popleft()
queue.popleft()
print(queue)


