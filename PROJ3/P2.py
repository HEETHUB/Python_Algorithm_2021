"""
**Instruction**
Please see instruction document.

"""
from BST_Helper import *
from typing import List
def P2(root: TreeNode) -> List[List[int]]:       
    ##### Write your Code Here #####
    result = []
    curLevel = [root]
    while curLevel:
        val = []
        nextLevel = []
        for n in curLevel:
            if n:
                val.append(n.val)
                nextLevel.append(n.left)
                nextLevel.append(n.right)
        if val:
            result.append(val)
        curLevel = nextLevel
    result.reverse()
    return result
    ##### End of your code #####