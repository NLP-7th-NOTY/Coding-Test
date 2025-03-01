import sys


def main():
    N = int(sys.stdin.readline().rstrip())
    tree = dict()
    
    for _ in range(N):
        node, left, right = sys.stdin.readline().rstrip().split()
        tree[node] = (left, right)
        
        
    def preorder(node):
        if node == '.':
            return ""
        
        return node + preorder(tree[node][0]) + preorder(tree[node][1])


    def inorder(node):
        if node == '.':
            return ""
        
        return inorder(tree[node][0]) + node + inorder(tree[node][1])


    def postorder(node):
        if node == '.':
            return ""
        
        return postorder(tree[node][0]) + postorder(tree[node][1]) + node
    
    print(preorder('A'))
    print(inorder('A'))
    print(postorder('A'))


if __name__ == "__main__":
    main()