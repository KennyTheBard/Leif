class Node:
	"""
	Linked list node
	"""
	def __init__(self, dataval=None):
		self.data = dataval
		self.next = None


class LinkedList:
	"""
	Linked list itself
	"""
	def __init__(self):
		self.head = None
		self.tail = None


class Queue:
	"""
	Queue implemented with a linked list
	"""
	def __init__(self):
		self.list = LinkedList()

	def push(self, item):
		if self.list.head == None:
			self.list.head = Node(item)
			self.list.tail = self.list.head
		else:
			node = Node(item)
			self.list.tail.next = node
			self.list.tail = node

	def pop(self):
		if not self.empty():
			node = self.list.head
			self.list.head = node.next
			return node.data
		return None

	def empty(self):
		return self.list.head == None
