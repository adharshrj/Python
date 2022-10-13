class Node:
    """
    A Node has data variable and an array of child nodes.
    """
    def __init__(self, data=None, children=None):
        self.data = data
        self.children = children

def preorder(root:Node) -> list:
    """
    Preorder traversal visits root node and then child in the children array
    >>>preorder([1,null,2,3,4,null,5,6,7])
    [1,2,5,6,7,3,4]
    """
    result = []

    def dfs(node: Node) -> None:
        if not node: return result

        result.append(node.data)
        for child in node.children:
            dfs(child)
    
    dfs(root)
    return result

def postorder(root:Node) -> list:
    """
    Postorder traversal visits child in the children array and then the root node
    >>>postorder([1,null,2,3,4,null,5,6,7])
    [5,6,3,2,4,1]
    """
    result = []

    def dfs(node: Node) -> None:
        if not node: return result

        for child in node.children:
            dfs(child)
        
        result.append(node.data)
    
    dfs(root)
    return result

def levelorder(root: Node) -> list[list[int]]:
    """
    Level order traversal visits the nodes in the tree level by level
    >>>levelorder([1,null,2,3,4,null,5,6,7])
    [[1],[2,3,4],[5,6,7]]
    """
        
    if not root: return []
        
    q = [(root)] # A deque from collections can also be used.
    result = []        
        
    while q:
        qlength = len(q)
        val = []
        for _ in range(qlength):
            node = q.pop(0)
            val.append(node.data)
                
            for child in node.children:
                q.append(child)
            
        result.append(val)
        
    return result

def main() -> None:  # Main function for testing.
    n = 3
    root = Node(n, 1)
    root.children[0] = Node(n, 2)
    root.children[1] = Node(n, 3)
    root.children[2] = Node(n, 4)
    root.children[0].children[0] = Node(n, 5)
    root.children[0].children[1] = Node(n, 6)
    root.children[0].children[2] = Node(n, 7)

    """All traversals of a n-ary tree"""

    print(f"Pre-order Traversal: {preorder(root)}")
    print(f"Post-order Traversal: {postorder(root)}", "\n")

    print(f"level-order Traversal: {levelorder(root)}", "\n")

if __name__ == "__main__":
    main()