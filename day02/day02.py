def deleteNode(deleteData) :
	global head, current, pre
	if head.data == deleteData :
		current = head
		head = head.link
		last = head
		while last.link = current :
			last = last.link
		last.link = head
		del(current)
		return

	current = head
	while current.link != head :
		pre = current
		current = current.link
		if current.data == deleteData :
			pre.link = current.link
			del(current)
			return
