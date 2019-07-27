#時複 O(n) 空複 O(1)
def fac(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a
#時複O(n)空複O(n)
def fac(n):#我能變的花招就是參數n
    if n==0 or n==1:
        return 1
    elif n>1:
        return n*fac(n-1)
    else:
        print('error')
print(fac(1))