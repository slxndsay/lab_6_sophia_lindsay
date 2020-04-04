# Lab 6
# Problem 1 and 2 
# Name: Sophia Lindsay

class Node():
	def __init__(self, data, nextPointer):
		self.data        = data
		self.nextPointer = nextPointer

	# Node Getters
	def getData(self):
		return(self.data)
	def getNext(self):
		return(self.nextPointer)

	# Node Setters
	def setData(self, d):
		self.data = d
	def setNext(self, n):
		self.nextPointer = n

class LinkedList():
	def __init__(self, head, size, tail):
		self.head = head
		self.size = size
		self.tail = tail


	# LinkedList Getters
	def getHead(self):
		return(self.head)
	def getSize(self):
		return(self.size)
	def getTail(self):
		return(self.tail)

	# LinkedList Setters
	def setHead(self, h):
		self.head = h
	def setSize(self, s):
		self.size = s
	def setTail(self, t):
		self.tail = t

	# Methods
	def isEmpty(self):
		if (self.size > 0): 
			return(True)
		return(False)


	def addNode(self, newData):
		if (self.size == 0):
			newNode = Node(data = newData, nextPointer = True)
	
			self.head = newNode
			self.size += 1 
	
		else:
			pass
		
def main():
	
	object1 = Node(data = "AU", nextPointer = True)
	object2 = LinkedList(head = None, size = 0, tail = None)

	print("LinkedList has", object2.head, 
			"head, a size of", object2.size)

	object2.addNode(newData = "GW")

	print("Now, LinkedList has head'", object2.head.data, "'and a size of ", object2.size)



if __name__ == "__main__":
	main()

