def dfs(node, path):

    if node is None:
        return

    # 1. 做选择
    path.append(node.val)

    # 2. 判断是否满足条件
    if is_leaf(node):
        process(path)

    # 3. 递归
    dfs(node.left, path)
    dfs(node.right, path)

    # 4. 撤销选择（回溯）
    path.pop()