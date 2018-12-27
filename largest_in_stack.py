class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

class MaxStack(object):
	def __init__(self):
		self.stack = Stack()
		self.maxes_stack = Stack()

	def push(self, item):
		self.stack.push(item)
		 if self.maxes_stack.peek() is None or item >= self.maxes_stack.peek():
            self.maxes_stack.push(item)

    def pop(self):
    	item = self.stack.pop()
    	if item == self.maxes_stack.peek():
        	self.maxes_stack.pop()
        return item

    def get_max():
    	return self.maxes_stack.peek()