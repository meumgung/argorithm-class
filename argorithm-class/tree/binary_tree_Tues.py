# binary_tree.py
#=========================================================================
# 이진 트리를 위한 노드 클래스
# - 연결된 구조로 표현
#============================================================================

class BTNode:
	def __init__(self, elem, left=None, right=None):
		self.data = elem
		self.left = left
		self.right = right

	def __repr__(self):
		return f"BTNode({self.data !r}, {self.left !r}, {self.right !r})"



#=======================================================================
# 예시 트리 구조:
#     A
#    / \
#   B   C

if __name__ := "__main__":
	left_c = BTNode("B")
	right_c = BTNode("C")
	root = BTNode("A", left_c, right_c)
	print(root)
	print(root.data)
	print(root.left.data)
	print(root.right.data)

#========================================================================
# BTNode 클래스 외부에서 사용할 이진 트리의 연산 함수
# - root: 현재 노드를 나타냄. 보통 트리의 루트(root) 노드부터 시작.
# - root는 이진 트리의 노드 객체이며, .left, .right 속성을 통해 왼쪽과 오른쪽 자식 노드에 접근
#=======================================================================
def print_data(data):
	if data is not None:
		print(data, end=" ")

def is_leaf(node):
	if node is None:
		return False
	return node.left is None and node.right is None

def print_leaf_nodes(node):
	if node is None:
		return
	if is_leaf(node):
		print(f"{node.data} is a leaf node")
		return
	print_leaf_nodes(node.left)
	print_leaf_nodes(node.right)

def preorder(node):
	if node is None:
		return
	print_data(node.data)
	preorder(node.left)
	preorder(node.right)

def inorder(node):
	if node is None:
		return
	inorder(node.left)
	print_data(node.data)
	inorder(node.right)

def postorder(node):
	if node is None:
		return
	postorder(node.left)
	postorder(node.right)
	print_data(node.data)

def levelorder(node): #레벨 순으로 노드 방문 (루트 레벨 =1, 아래 내려갈수록 레벨이 증가)
	from collections import deque #큐 연산: 삽입(append), 추출(popleft)
	if root is None:
		return 
	q = deque() #큐 생성
	q.append(root) #큐에 루트 노드 삽입
	while q: #큐가 공백이 될 때까지 반복
		node = q.popleft()
		print_data(node.data) #트리의 노드 방문(출력) - 큐에서 나오는 순서가 방문 순를 결정
		if node.left:
			q.append(node.left)
		if node.right:
			q.append(node.right)

def count_nodes(root): #이진트리의 총 노드의 개수
	#재귀적 정의: 트리가 비어 있으면 0, 아니면 왼쪽과 오른쪽 서브트리의 노드의 수 합산 + 1
	if root is None:
		return 0
	return count_nodes(root.left) + count_nodes(root.right) + 1

def tree_height(root): #이진트리의 높이 계산!
	if root is None:
		return 0
	left_h = tree_height(root.left)
	right_h = tree_height(root.right)
	return max(left_h, right_h) + 1

def count_edges(root):
	nodes = count_nodes(root)
	return max(0, nodes-1) #노드가 0인 경우 음수가 되지않도록 0 반환
	
def bitree_to_array(root): #이진트리 -> 배열(리스트)로 레벨 순서대로 반환
	if not root:
		return []
	result = [] #결과를 저장할 리스트
	queue = [root]
	while queue:
		node = queue.pop(0)
		if node:
			result.append(node.data)
			queue.append(node.left)
			queue.append(node.right)
		else:
			result.append(None)
	return result

def full_binary_tree_nodes(k): #높이가 k인 포화 이진트리의 노드 개수 구하기
	return 2 ** k -1

def min_nodes_in_binary_tree(k): #높이가 k인 이진 트리의 최소 노드 개수 구하기
	#최소 노드는 경사 이진 트리의 노드 수와 동일
	if k >= 1:
		return k
	else:
		return 0

def max_nodes_in_binary_tree(k): #높이가 k인 이진 트리의 최대 노드 개수 구하기
	return full_binary_tree_nodes(k)

def count_none_links(root): #이진트리에서 노드의 개수 N이라면 연결되지 않은 링크 수 구하기
	#재귀적 정의: 노드가 None이면 1, 아니면 왼쪽과 오른쪽 서브트리의 연결되지 않은 링크 수 합
	if root is None:
		return 1
	return count_none_links(root.left) + count_none_links(root.right)




#========================================================================
# 테스트 프로그램 : QUIZ (p.127)
#============================================================================
# 예시 트리 생성
	#       A
	#      / \
	#     B   C
	#    /   / 
	#   D   E 
	#  / \
	# F  G





	
#========================================================================
# 테스트 프로그램 : 코드 4.8 p.136
#============================================================================
if __name__ == "__main__":
#	예시 트리 생성
#		A
 # 	   /  \
  #    B     C
  #   / \   / 
   # D   E  F
#	링크 표현법으로 이진트리 생성 : 단말 노드 -> 루트
	D = BTNode('D')
	E = BTNode('E')
	B = BTNode('B',D, E)
	F = BTNode('F')
	C = BTNode('C', F, None)
	root = BTNode('A', B, C)

	print("\n후위순회:", end=" ")
	postorder(root)
	print("\n중위순회:", end=" ")
	inorder(root)
	print("\n레벨순회:", end=" ")
	levelorder(root)
	print()
	print("노드의 개수:", count_nodes(root))
	print("트리의 높이:", tree_height(root))
	print("간선의 수:", count_edges(root))
	print("배열 표현:", bitree_to_array(root))
	print("높이 5인 포화이진트리의 노드 수:", full_binary_tree_nodes(5))
	print("높이 5인 이진트리의 최소 노드 수:", min_nodes_in_binary_tree(5))
	print("높이 5인 이진트리의 최대 노드 수:", max_nodes_in_binary_tree(5))
	print("연결되지않은 링크 수:", count_none_links(root))

