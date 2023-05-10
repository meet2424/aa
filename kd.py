import numpy as np

class KDNode:
  def __init__ (self, data, depth=0, left=None, right=None): 
    self.data = data
    self.depth = depth 
    self.left = left 
    self.right = right

def insert(node, point): 
  if node is None:
    return KDNode(point)
    
  cd = node.depth % 2 # 2-dimensional space 

  if point[cd] < node.data[cd]:
    node.left = insert(node.left, point) 
    node.left.depth = node.depth + 1
  else:
    node.right = insert(node.right, point) 
    node.right.depth = node.depth + 1

  return node

def build_balanced_kdtree(points, depth=0): 
  n = len(points)

  if n <= 0:
    return None

  cd = depth % 2 # 2-dimensional space 
  median_idx = n // 2

  sorted_points = points[np.argsort(points[:,cd])] 
  median = sorted_points[median_idx]

  node = KDNode(median, depth)
  node.left = build_balanced_kdtree(sorted_points[:median_idx], depth + 1)
  node.right = build_balanced_kdtree(sorted_points[median_idx+1:], depth + 1)
  
  return node 
  
def inorder(node):
  if node is not None:  
    inorder(node.left)
    print(f"Depth: {node.depth}, Data: {node.data}, Left: {node.left.data if node.left else None}, Right: {node.right.data if node.right else None}")
    inorder(node.right)


# Sample input for unbalanced tree
unbalanced_points = np.array([[6, 2], [7, 1], [2, 9], [3, 6], [4, 8], [8, 4], [5, 3], [1, 5], [9, 5]])
unbalanced_root = KDNode(unbalanced_points[0])

for point in unbalanced_points[1:]: 
  insert(unbalanced_root, point)
  
print("Unbalanced KD-Tree (inorder traversal):") 
inorder(unbalanced_root)

# Sample input for balanced tree
balanced_points = np.array([[6, 2], [7, 1], [2, 9], [3, 6], [4, 8], [8, 4], [5, 3], [1, 5], [9, 5]])
sorted_points = balanced_points[np.argsort(balanced_points[:,0])] 
balanced_root = build_balanced_kdtree(sorted_points)

print("\nBalanced KD-Tree (inorder traversal):") 
inorder(balanced_root)