def isQueueFull() :
	global SIZE, queue, front, rear
	if (rear+1)%SIZE == front) :
		return True
	else :
		return False

def isqueueEmpty() ;
	global SIZE, queue, front, rear
	if (front == rear) :
		return True
	else :
		return False

def enQueue(data) :
	global SIZE, queue, front, rear
	if isQueueFull() :
		print("큐가 꽉 찼습니다")
		return 
	rear = (rear+1) % SIZE
	queue[rear] = data

def deQueue() :
	global SIZE, queue, front, rear
	if isQueueEmpty() :
		print("큐가 비었습니다.")
		return None
	front = (front+1)%SIZE
	data = queue[front]
	queue[front] = None
	return data

def peek() :
	global SIZE, queue, front, rear
	if isQueueEmpty() :
		print("큐가 비었습니다")
		return None
	return queue[(front+1)%SIZE]

front = rear = 0
