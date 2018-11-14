class cards():
	def__init__(self, suit, numbers):
		self.suit = suit 
		self.numbesr = numbers 

class deck_of_cards():
	cards_list = []

	def__init__(self):
		self.construct():

	def construct(self):
		for i in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
			for j in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
				self.cards_list.append(cards(i,j))

	def shuffle(self):
		return random.shuffle()

class Node():
	def__init__(self, data):
		self.data = data 

class stack():
	def__init__(self):
		self.head = None 

	def push(self, data):
		if self.head is None:
			self.head = data
		else:
			new_node = Node(data)
			new_node.next = self.head 
			self.head = new_node 

	def pop(self):
		if self.head is None:
			return None 
		else:
			popped = self.head.data
			self.head = self.head.next
			return popped 

class stack():
	def__init__(self):
		self.stack = list()

	def push(self, data):
		if data not in self.stack:
			self.stack.append(data)
			return True 
		return False

	def pop(self):
		if len(self.stack) <= 0:
			return "Stack is empty"
		else:
			return self.stack.pop()

class queue():
	def__init__(self):
		self.items = [] 

	def enqueue(self, data):
		self.items.insert(0, data)

	def dequeue(self):
		return self.head.data 

class Nodelist():
	def__init__(self, data):
		self.data = data 
		self.next = None 

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, new_node):
		self.next = new_node


class Linkedlist():
	def__init__(self):
		self.head = None 

	def insert(self, data):
		if self.head is None:
			self.head =data
		else:
			new_node = Nodelist(data)
			new_node.set_next(self.head) 
			self.head = new_node 

	def size(self):
		current = self.head
		count = 0 
		while current:
			count += 1 
			current = current.get_next()
		return count 

	def search(self, data):
		current = self.head 
		found = False
		while current & found is False:
			if current.get_data() == data:
				found = True 
			else:
				current = current.get_next()
		if current is None:
			return "Error"
		return current 

	def delete(self, data):
		current = self.head 
		found = False
		previos = None 
		while current & found is False:
			if current.get_data() == data:
				found = True 
			else:
				previos = current
				current = current.get_next()
		if current is None:
			return "Error"
		if previos is None:
			self.head = current.get_next()
		else:
			previos.set_next(current.get_next())

class node():
	def__init__(self, data, lchild, rchild):
		self.data = data 
		self.lchild = None 
		self.rchild = None 

class searchtree():
	def__init__(self):
		self.root = None 

	def create(self, data):
		if self.root is None:
			self.root = node(data)
		else:
			current = self.root 
			while True:
				if data < current.data:
					if current.left:
						current = current.left
					else:
						current.left = node(data) 
						break 
				elif data > current.data:
					if current.right:
						current = current.right
					else:
						current.right = node(data)
						break 
				else:
					break

	def insert(root, val):
		if root is None:
			root = val
		else:
			if root.data < val:
				if root.rchild == None:
					root.rchild = node(val) 
				else:
					insert(root.rchild, val)
			if root.data > val:
				if root.lchild == None:
					root.lchild = node(val)
				else:
					insert(root.lchild, val)





