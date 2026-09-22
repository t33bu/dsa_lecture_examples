class Queue:
    data = deque()                   // backed by doubly linked list

    function enqueue(value):
        data.appendRight(value)      // O(1)

    function dequeue():
        if isEmpty(): error
        return data.removeLeft()     // O(1)

    function peek():
        return data.first            // O(1)

    function isEmpty():
        return len(data) == 0        // O(1)
				