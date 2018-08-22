def fibRecursive(n):
    if n in [1, 0]:
        return n
    return fibRecursive(n - 1) + fibRecursive(n - 2)
