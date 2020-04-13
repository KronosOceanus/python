'''自定义栈'''
class Stack:
    def __init__(self, size=10):
        self._content = []
        self._size = size
        self._current = 0

    def __del__(self):
        del self._content

    def empty(self):
        self._content = []
        self._current = 0

    def isEmpty(self):
        return not self._content

    def setSize(self, size):
        if size < self._size:
            for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size

    def isFull(self):
        return self._current == self._size

    def push(self, v):
        if self._current < self._size:
            self._content.append(v)
            self._current += 1
        else:
            print('栈满')

    def pop(self):
        if self._content:
            self._current -= 1
            return self._content.pop()
        else:
            print('栈空')

    def show(self):
        print(self._content)