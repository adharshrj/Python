class Node:
    """
    A Node has data variable and an array of child nodes.
    """
    def __init__(self, data=None, children=None):
        self.data = data
        self.children = children


def depth_of_nary_tree(root: Node) -> int:
    """
    Iterative function that gives the depth of the nary tree

    >>> root = [1,null,2,3,4,null,5,6,7]
    >>> depth_of_nary_tree(root)
    3

    Process is continued if the child has any children.
    """
    if not root: return 0
        
    q = [(root, 1)] # A deque from collections can also be used.
    maxdepth = 0
        
    while q:
        node, depth = q.pop(0)
            
        if node and node.children:
            for child in node.children:
                q.append((child, depth + 1))
            
        maxdepth = max(depth, maxdepth)
        
    return maxdepth

def main() -> None:  # Main function for testing.
    n = 3
    root = Node(n, 1)
    root.children[0] = Node(n, 2)
    root.children[1] = Node(n, 3)
    root.children[2] = Node(n, 4)
    root.children[0].children[0] = Node(n, 5)
    root.children[0].children[1] = Node(n, 6)
    root.children[0].children[2] = Node(n, 7)
    print(f"Depth of an n-ary tree: {depth_of_nary_tree(root)}")


if __name__ == "__main__":
    main()