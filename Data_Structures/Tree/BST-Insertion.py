def insert(root,node):
    if root is None:
        root = node

    else:
        if root.val<node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)
