def isQueneFull() :
	global SIZE, queue, front, rear
	if rear != SIZE-1 :
		return False
	elif (rear == SIZE-1) and (front == -1) :
		return True
	else :
		for i in range(front+1, SIZE) :
			queue[i-1] = queue[i]
			queue[i] = None
		front -= 1
		rear -= 1
		return False

def isQueueEmpty() :
	global SIZE, queue, front, rear
	if front == rear :
		return True
	else :
		return False

def enQueue(data) :
	global SIZE, queue, front, rear
	if (isQueueFill()) :
		print("큐가 꽉 찼습니다.")
		return 
	rear += 1
	queue[rear] = data

def deQueue() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print("큐가 비었습니다.")
		return None
	front += 1
	data = queue[front]
	queue[front] = None
	return data

def peek() :
	global SIZE, queue, front, rear
	if isQueueEmpty() :
		print("큐가 비었습니다.")
		return None
	return queue[front+1]

front = rear = -1
