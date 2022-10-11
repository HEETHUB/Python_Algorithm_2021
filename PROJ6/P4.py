def P4(nums:list)->set:
    # write your code below
    ans = set()
    for num in nums:
        if num in ans:
            ans.remove(num)
        else:
            ans.add(num)
    return ans