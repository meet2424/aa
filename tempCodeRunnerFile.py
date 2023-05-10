def traverse_in_order(curr):
    if curr is None:
        return
    traverse_in_order(curr.left)
    print(f"({', '.join(map(str, curr.nums))}) ", end="")
    traverse_in_order(curr.right)