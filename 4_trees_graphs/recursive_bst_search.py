# Uses https://pypi.org/project/binarytree/
from binarytree import bst

my_bst = bst(height=5)
print(my_bst)

def recursive_bst_search(v, target):
    if v == None:
        print('Not found',target)
        return None
    # Print search path
    print(v.value)
    if v.value == target:
        print('Found',target)
        return v.value
    elif v.value > target:
        return recursive_bst_search(v.left, target)
    else:
        return recursive_bst_search(v.right, target)

recursive_bst_search(my_bst,17)
