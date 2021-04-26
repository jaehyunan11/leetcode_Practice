class FileSystem:

    def __init__(self):
        self.paths = defaultdict()

    def createPath(self, path: str, value: int) -> bool:
        # step-1 : basic path validations
        if path == "/" or len(path) == 0 or path in self.paths:
            return False
        # step-2 : if the parent doesn't exist. Note that "/" is a valid parent.
        parent = path[:path.rfind('/')]
        if len(parent) > 1 and parent not in self.paths:
            return False
        # step-3 : add this new path and return true.
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)

    # TIME : O(M) M is length of path
    # SPACE : O(K) K the number of unique paths that we add.
