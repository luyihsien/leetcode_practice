class Solution:
    def subsets(self, nums:'list[int]'):#-> List[List[int]]
        res = []
        n = len(nums)

        def helper(i, tmp):
            print('helper({},{})'.format(i,tmp))
            res.append(tmp)
            print('res',res)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        #res.sort()#Solution().subsets([3,2,1])) 輸出變[[], [1], [2], [2, 1], [3], [3, 1], [3, 2], [3, 2, 1]]
        return res
print(Solution().subsets([3,2,1]))#[[], [3], [3, 2], [3, 2, 1], [3, 1], [2], [2, 1], [1]]
"""
helper(0,[])
res [[]]
helper(1,[3])
res [[], [3]]
helper(2,[3, 2])
res [[], [3], [3, 2]]
helper(3,[3, 2, 1])
res [[], [3], [3, 2], [3, 2, 1]]
helper(3,[3, 1])
res [[], [3], [3, 2], [3, 2, 1], [3, 1]]
helper(2,[2])
res [[], [3], [3, 2], [3, 2, 1], [3, 1], [2]]
helper(3,[2, 1])
res [[], [3], [3, 2], [3, 2, 1], [3, 1], [2], [2, 1]]
helper(3,[1])
res [[], [3], [3, 2], [3, 2, 1], [3, 1], [2], [2, 1], [1]]
[[], [3], [3, 2], [3, 2, 1], [3, 1], [2], [2, 1], [1]]

"""
