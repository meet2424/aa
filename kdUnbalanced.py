from _future_ import annotations

class KDNode:
  data: list[int] = []
  left: KDNode = None
  right: KDNode = None

  def _init_(self, data: list[int]):
    self.data = data
    self.left = None
    self.right = None

class KDTree:
  root: KDNode = None
  dimension: int = 0

  def _init_(self, dimension = 2):
    self.root = None
    self.dimension = dimension

  def insert(self, data: list[int]):
    self.root = self._insert(data, 0, self.root)

  def _insert(self, data: list[int], index: int, current):
    if not current:
      return KDNode(data)
    else:
      if data[index] < current.data[index]:
        current.left = self._insert(data, (index + 1) % self.dimension, current.left)
      else:
        current.right = self._insert(data, (index + 1) % self.dimension, current.right)
    return current

  def inorder(self):
    self._inorder(self.root)

  def _inorder(self, current):
    if current:
      self._inorder(current.left)
      print(current.data)
      self._inorder(current.right)

  @staticmethod
  def create_balanced_tree(data: list[list[int]]) -> KDTree:
    k = len(data[0])
    tree = KDTree(k)

    def _sort(_data: list[list[int]], index = 0):
      if len(_data) == 1:
        tree.insert(_data[0])
        return
      _sorted_data = sorted(_data, key=lambda x: x[index])
      if len(_data) == 2:
        tree.insert(_sorted_data[0])
        tree.insert(_sorted_data[1])
        return
      mid = len(_sorted_data) // 2
      median_element = _sorted_data[mid]
      print(f"Median element: {median_element}, index: {index}")
      tree.insert(median_element)
      right_splitting_index = mid + 1 if len(_sorted_data[mid:]) > 1 else 1
      print(_sorted_data[:mid])
      print(_sorted_data[right_splitting_index:])
      _sort(_sorted_data[:mid], (index + 1) % k)
      _sort(_sorted_data[right_splitting_index:], (index + 1) % k)

    _sort(data)
    return tree

  def print_tree(self):
    self._print_tree(self.root, 0, "R")

  def _print_tree(self, node: KDNode, depth: int, label: str):
    if not node:
      Return


    print(" " * depth, end="")
    print(f"{label}->{node.data}")
    self._print_tree(node.left, depth + 1, "L")
    self._print_tree(node.right, depth + 1, "R")


data = [[6, 2], [7, 1], [2, 9], [3, 6], [4, 8], [8, 4], [5, 3], [1, 5], [9, 5]]

kd_tree = KDTree(2)
kd_tree = KDTree.create_balanced_tree(data)

# for point in data:
  # kd_tree.insert(point)

# kd_tree.inorder()
kd_tree.print_tree()
