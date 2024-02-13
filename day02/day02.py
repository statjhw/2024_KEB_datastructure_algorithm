class Node :
	def __init(self) :
		self.data = None
		self.link = None

def printNodes(start) :
	current = start
	if current.link == None :
		return
	print(current.data, end = ' ')
	while current.link != start :
		current = current.link
		print(current.data, end = ' ')
	print()

head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__" :
	
	node = Node()
	node.data = dataArray[0]
	head = node
	node.link = head

	for data in dataArray[1:]:
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		node.link = head
		
printNodes(head)
