"""
**Instruction**
Please see instruction document.

"""
from BST_Helper import *
def P1(root: TreeNode, x:int) -> int:       
    ##### Write your Code Here #####
    if root:
        curNode = root
        while curNode.val != x:
            if x > curNode.val:
                curNode = curNode.right
            elif x < curNode.val:
                curNode = curNode.left
            if curNode == None:
                return 0
        total = 0
        result = list()
        thislevel = [curNode]
        while thislevel:
            nextlevel = list()
            none_list=1
            for n in thislevel:
                if n !=None:
                    none_list=0
                    break
            if none_list==1:
                break

            for n in thislevel:
                if n != None: 
                    result.append(n.val)
                    nextlevel.append(n.left)
                    nextlevel.append(n.right)
                else:
                    result.append(None)
                    nextlevel.append(None)
                    nextlevel.append(None)        
                thislevel = nextlevel
        for num in result:
            if num:
                total += num
        total -= result[0]
        return total
    else:
        return 0
    ##### End of your code #####
