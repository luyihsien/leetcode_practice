board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
a=[[0,0]]
b=[]
c=''
class Solution:
    def alphabetBoardPath(self, target: str):
        for i in target:
            print('i',i)
            for j in range(len(board)):
                for k in range(len(board[j])):
                    print(board[j][k])
                    if i==board[j][k]:
                        a.append([j,k])
        print(a)
        for m in range(len(a)-1):
            b.append([a[m+1][0]-a[m][0],a[m+1][1]-a[m][1]])
        print(b)
        global c
        for i in range(len(b)):
            print('b[i]',b[i])
            if b[i][0]>0:
                c += 'R' * abs(b[i][0])
            if b[i][0] < 0:
                c += 'L' * abs(b[i][0])
            if b[i][1] > 0:
                c += 'U' * abs(b[i][1])
            if b[i][1] < 0:
                c += 'D' * abs(b[i][1])
            c+='!'
        return c


print(Solution().alphabetBoardPath("leet"))