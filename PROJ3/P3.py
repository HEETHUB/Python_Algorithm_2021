"""
**Instruction**
Please see instruction document.
"""
from BST_Helper import *
def P3(root: TreeNode, val: int) -> TreeNode:    
    ##### Write your Code Here #####
    curNode = root
    curRoot = root
    while curNode:
        if val < curNode.val:
            if curNode.right and curNode.left:
                curNode = curNode.left
            elif curNode.right:
                curNode.left = TreeNode(val)
                break
            elif curNode.left:
                if val < curNode.left.val:
                    curNode.right = TreeNode(curNode.val)
                    curNode.val, curNode.left.val = curNode.left.val, val
                else:
                    curNode.right = TreeNode(curNode.val)
                    curNode.val = val
                break
            else:
                if val > curRoot.val:
                    curRoot.val, val = val, curRoot.val
                    curNode = curRoot
                else:
                    curRoot = root.left
                    curNode = curRoot
        elif val > curNode.val:
                if curNode.right and curNode.left:
                    curNode = curNode.right
                elif curNode.left:
                    curNode.right = TreeNode(val)
                    break
                elif curNode.right:
                    if val > curNode.right.val:
                        curNode.left = TreeNode(curNode.val)
                        curNode.val, curNode.right.val = curNode.right.val, val
                    else:
                        curNode.left = TreeNode(curNode.val)
                        curNode.val = val
                    break
                else:
                    if val < curRoot.val:
                        curRoot.val, val = val, curRoot.val
                        curNode = curRoot
                    else:
                        curRoot = root.right
                        curNode = curRoot
    return root
    ##### End of your code #####


