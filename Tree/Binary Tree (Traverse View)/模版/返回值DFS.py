def dfs(node):
    if node is None:
        return base_value

    left = dfs(node.left)
    right = dfs(node.right)

    result = combine(left, right)

    return result