class Solution:
    def largestUniqueNumber(self, A) -> int:
        if A==[]:
            return -1
        A.sort()
        d={}
        for i in A:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        while 1:
            if A==[]:
                return -1
            elif d[max[A]]!=1:
                A=A[:len(A)-d[max[A]]]
            else:
                return max[A]
Solution().largestUniqueNumber([9,9,8,8])