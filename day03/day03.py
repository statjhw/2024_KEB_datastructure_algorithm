#깊이 우선 탐색 재귀를 이용한 
# def dfs(g, v, visited) :
#     visited[v] = True
#     print(name[v], end = ' ')
#     for i in range(len(g)) :
#         if g[v][i] == True and not visited[i] :
#             dfs(g, i, visited)

#이진 탐색 트리에서 데이터를 삽입하는 방법
# class TreeNode :
# 	def __init__(self) :
# 		self.left = None
# 		self.data = None
# 		self.right = None

# memory = []
# root = None
# nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

# node = TreeNode()
# node.data = nameAry[0]
# root = node

# for name in nameAry[1:] :
# 	node = TreeNode()
# 	node.data = name
# 	current = root
# 	while True :
# 		if name < current.data :
# 			if current.left == None :
# 				current.left = node
# 				break
# 			current = current.left
# 		else :
# 			if current.right == None :
# 				current.right = node
# 				break
# 			current = current.right
	


# findName = '마마무'
# current = root 
# while True :
# 	if findName == current.data :
# 		print(findName, "을 찾음")
# 		break
# 	elif findName < current.data :
# 		if current.left == None :
# 			print(findName, '이 트리에 없음')
# 			break
# 		current = current.left
# 	else :
# 		if current.right == None :
# 			print(findName, '이 트리에 없음')
# 			break
# 		current = current.right

# #이진 탐색 트리에서 데이터 삭제 완성

# deleteName = '마마무'
# current = root
# parent = None
# while True :
# 	if deleteName == current.data :
# 		if current.left == None and current.right == None :
# 			if parent.left == current :
# 				parent.left = None
# 			else : 
# 				parent.right = None
# 			del(current)
# 		elif current.left != None and current.right == None :
# 			if parent.left == current :
# 				parent.left = current.left 
# 			else :
# 				parent.right = current.left
# 			del(current)

# 		elif current.left  == None and current.right != None :
# 			if parent.left == current :
# 				parent.left = current.right
# 			else :
# 				parent.right = current.right
# 			del(current)
		

# 		print(deleteName, "이 삭제됨.")
# 		break
# 	elif deleteName < current.data :
# 		if current.left == None :
# 			print(deleteName, '이 트리에 없음')
# 			break
# 		parent = current
# 		current = current.left
# 	else :
# 		if current.right == None :
# 			print(deleteName, '이 트리에 없음')
# 			break
# 		parent = current
# 		current = current.right






 


#그래프
class Graph() :
	def __init__(self, size) -> None:
		self.SIZE = size
		self.graph = [[0 for _ in range(self.SIZE)] for _ in range(self.SIZE)]

G1, G3 = None, None

G1 = Graph(4)
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print("##G1 무방향 그래프")
for row in range(G1.SIZE) :
	for col in range(G1.SIZE) :
		print(G1.graph[row][col], end = " ")
	print()

G3 = Graph(4)
G3.graph[0][1] = 1; G3.graph[0][2] = 1
G3.graph[3][0] = 1; G3.graph[3][2] = 1

print("##G3 방향 그래프")
for row in range(G3.SIZE) :
	for col in range(G3.SIZE) :
		print(G3.graph[row][col], end = " ")
	print()



