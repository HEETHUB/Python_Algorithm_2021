from typing import List
def P2(n: int, edges: List[tuple]) -> int:
    ##### Write your Code Here #####
    if n <= 1:
        return 1
    ans = set()
    for edge in edges:
        if 1 in edge:
            for num in edge:
                ans.add(num)
    
    for edge in edges:
        for num in edge:
            if num in ans:
                for n in edge:
                    ans.add(n)
    return len(ans)
    ##### End of your code #####