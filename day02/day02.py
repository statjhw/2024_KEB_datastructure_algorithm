class Node() :
	def __init__(self):
		self.data = None
		self.link = None


def insertNode(findData, insertData) :
	global memory, head, current, pre
	if head.data == findData :
		node = Node()
		node.data = insertData
		node.link = head
		last = head
		#마지막 노드 찾기
		while last.link != head :
			last = last.link
		last.link = node
		head = node
		return

	current = head
	while current.link != head :
		pre = current 
		current = current.link
		if current.data == findData :
			node = Node()
			node.data = insertData
			node.link = current
			pre.link = node
			return

	node = Node()
	node.data = insertData
 	current.link = node
	node.link = head

