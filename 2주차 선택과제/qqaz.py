class ListQueue(object):
    def _init_(self):
        self.queue = []

    def pop(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)

    def push(self, n):
        self.queue.append(n)
        pass

    def printQueue(self):
        print(self.queue)
