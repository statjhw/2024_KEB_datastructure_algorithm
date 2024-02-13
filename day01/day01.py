import mymath
import time
import random

## 단순 연결 리스트
## 클래스와 함수 선언 부분 ##
# class Node() :
# 	def __init__ (self) :
# 		self.data = None
# 		self.link = None
#
# def printNodes(start) :
# 	current = start
# 	if current is None:
# 		return
# 	print(current.data, end = ' ')
# 	while current.link != None:
# 		current = current.link
# 		print(current.data, end = ' ')
# 	print()
#
# ## 전역 변수 선언 부분 ##
# memory = []
# head, current, pre = None, None, None
# dataArray = ["다현", "정연", "쯔위", "사나", "지효", '현우']
#
# ## 메인 코드 부분 ##
# if __name__ == "__main__" :
#
# 	node = Node()		# 첫 번째 노드
# 	node.data = dataArray[0]
# 	head = node
# 	memory.append(node)
#
# 	for data in dataArray[1:] :	# 두 번째 이후 노드
# 		pre = node
# 		node = Node()
# 		node.data = data
# 		pre.link = node
# 		memory.append(node)
#
# 	printNodes(head)
# 객체의 얇은 복사 시 문제가 생기는 부분


## 클래스와 함수 선언 부분 ##
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

# def printNodes(start) :
#     current = start
#     if current == None :
#         return
#     print(current.data, end = ' ')
#     while current.link != None:
#         current = current.link
#         print(current.data, end = ' ')
#     print()
#
# def make_simple_linked_list(namePhone) :
#     global memory, head, current, pre
#     printNodes(head)
#
#     node = Node()
#     node.data = namePhone
#     memory.append(node)
#     if head == None :			# 첫 번째 노드일 때
#         head = node
#         return
#
#     if head.data[1] > namePhone[1] :	# 첫 번째 노드보다 작을 때
#         node.link = head
#         head = node
#         return
#
#     # 중간 노드로 삽입하는 경우
#     current = head
#     while current.link != None :
#         pre = current
#         current = current.link
#         if current.data[1] > namePhone[1]:
#             pre.link = node
#             node.link = current
#             return
#
#     # 삽입하는 노드가 가장 큰 경우
#     current.link = node
#
# ## 전역 변수 선언 부분 ##
# memory = []
# head, current, pre = None, None, None
# dataArray = [["지민", 180], ["정국", 177], ["뷔", 183], ["슈가", 175], ["진", 179]]
#
# ## 메인 코드 부분 ##
# if __name__ == "__main__" :
#
# 	for data in dataArray :
# 		make_simple_linked_list(data)
#
# 	printNodes(head)


class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None
def insertNode(findData, insertData) :
	global memory, head, current, pre

	if head.data == findData :		# 첫 번째 노드 삽입
		node = Node()
		node.data = insertData
		node.link = head
		last = head		# 마지막 노드를 첫 번째 노드로 우선 지정
		while last.link != head :	# 마지막 노드를 찾으면 반복 종료
			last = last.link	# last를 다음 노드로 변경
		last.link = node		# 마지막 노드의 링크에 새 노드 지정
		head = node
		return

	current = head
	while current.link != head :		# 중간 노드 삽입
		pre = current
		current = current.link
		if current.data == findData :
			node = Node()
			node.data = insertData
			node.link = current
			pre.link = node
			return

	node = Node()			 # 마지막 노드 삽입
	node.data = insertData
	current.link = node
	node.link = head
def printNodes(start):
	current = start
	if current.link == None :
		return
	print(current.data, end=' ')
	while current.link != start:
		current = current.link
		print(current.data, end=' ')
	print()

def findNode(findData) :
	global memory, head, current, pre

	current = head
	if current.data == findData :
		return current
	while current.link != head :
		current = current.link
		if current.data == findData :
			return current
	return Node()	# 빈 노드 반환


def deleteNode(deleteData) :
    global memory, head, current, pre

    if head.data == deleteData :         # 첫 번째 노드 삭제
        current = head
        head = head.link
        while last.link != current :
            last = last.link
        last.link = head
        del(current)
        return

    current = head                          # 첫 번째  외 노드 삭제
    while current.link != head :
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            return


def count(head) :
	current = head
	even_count = 0
	odd_count = 0
	if current.data % 2 == 0:
		even_count += 1
	else:
		odd_count += 1
	current = current.link
	while current != head :
		if current.data % 2 == 0 :
			even_count += 1
		else :
			odd_count += 1
		current = current.link

	if even_count > odd_count :
		return 0
	else :
		return 1

def change() :
	global head, current
	if count(head) == 0 :
		current = head
		if (current.data % 2 == 0) :
			current.data *= -1
		current = current.link

		while current != head :
			if current.data %2 == 0 :
				current.data *= -1
			current = current.link

	else :
		current = head
		if (current.data % 2 == 1):
			current.data *= -1
		current = current.link

		while current != head:
			if current.data % 2 == 1:
				current.data *= -1
			current = current.link



import random

if __name__ == "__main__" :
	dataArray = [random.randint(0,100) for _ in range(7)]

	node = Node()
	node.data = dataArray[0]	# 첫 번째 노드
	head = node
	node.link = head


	for data in dataArray[1:] :	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		node.link = head

	printNodes(head)

	change()

	printNodes(head)





