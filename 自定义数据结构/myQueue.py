'''队列'''
class myQueue:
    def __init__(self, size=10):
        self._content = []
        self._size = size
        self._current = 0

    def __del__(self):
        del self._content

    def setSize(self, size):
        if size < self._current:    #缩小队列，删除后端元素
            for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
            self._size = size

    def put(self, v):
        if self._current < self._size:
            self._content.append(v)
            self._current += 1
        else:
            print('队列已满')

    def get(self):
        if self._content:
            self._current -= 1
            return self._content.pop(0)
        else:
            print('队列已空')

    def show(self):
        if self._content:
            print(self._content)
        else:
            print('队列已空')

    def empty(self):
        self._content = []
        self._current = 0

    def isEmpty(self):
        return self._current == 0

    def isFull(self):
        return self._current == self._size

