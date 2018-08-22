def isBinarySearchTree(root,
                       lowerBound = -float('inf'),
                       upperBound = float('inf')):
    if not root:
        return True

    if (root.value >= upperBound or root.value <= lowerBound):
        return False

    return (isBinarySearchTree(root.left, lowerBound, root.value)
            and isBinarySearchTree(root.right, root.value, upperBound))

