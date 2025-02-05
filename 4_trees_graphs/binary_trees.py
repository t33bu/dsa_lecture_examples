# Uses https://pypi.org/project/binarytree/
from binarytree import Node

'''
btree = Node('a')
btree.left = Node('b')
btree.right = Node('c')
btree.left.left = Node('d')
btree.left.right = Node('e')
btree.right.left = Node('f')
btree.right.right = Node('g')
print(btree)
print(list(btree))
print(btree.values)

'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(root) 

print('inorder',root.inorder)
print('preorder',root.preorder)
print('postorder',root.postorder) 
print('levelorder',root.levelorder) 
# print(list(root)) # sam as root.levelorder
'''
def preorder(node):
    if node == None:
        return
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right) 

def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right) 

def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right) 
    print(node.value, end=" ")

print('preorder:',end=' ')
preorder(root)
print('\ninorder:',end=' ')
inorder(root)
print('\npostorder:',end=' ')
postorder(root)
'''