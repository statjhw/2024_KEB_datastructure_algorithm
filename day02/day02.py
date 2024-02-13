class TreeNode() :
	def __init__(self) :
		self.left = None
		self.data = None 
		self.right = None

def preorder(node) :
	if node == None :
		return 
	print(node.data, end = '->')
	preorder(node.left)
	preorder(node.right)

def inorder(node) :
	if node == None :
		return 
	inorder(node.left)
	inorder(node.data, end = '->')
	inorder(node.right)
	
def postorder(node) :
	if node == Node :
		return 
	postorder(node.left)
	postorder(node.right)
	print(node.datam end = '->')
