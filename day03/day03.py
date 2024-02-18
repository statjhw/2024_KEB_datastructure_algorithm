#깊이 우선 탐색 재귀를 이용한 
# def dfs(g, v, visited) :
#     visited[v] = True
#     print(name[v], end = ' ')
#     for i in range(len(g)) :
#         if g[v][i] == True and not visited[i] :
#             dfs(g, i, visited)

#이진 탐색 트리에서 데이터를 삽입하는 방법
class TreeNode :
	def __init__(self) :
		self.left = None
		self.data = None
		self.right = None

memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

node = TreeNode()
node.data = nameAry[0]
root = node

for name in nameAry[1:] :
	node = TreeNode()
	node.data = name
	current = root
	while True :
		if name < current.data :
			if current.left == None :
				current.left = node
				break
			current = current.left
		else :
			if current.right == None :
				current.right = node
				break
			current = current.right
	






