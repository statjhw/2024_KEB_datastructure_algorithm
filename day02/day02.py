def findNode(findData) :
	global head, current, pre

	current = head
	if current.data == findData :
		return current
	while current.link != head :
		current = current.link
		if current.data == findData :
			return current
		
	return Node()

:
