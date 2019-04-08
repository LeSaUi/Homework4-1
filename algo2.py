'''

def maxSum(n,a,b):
    if a==b:return n[a],a,b
    m1,m2=(a+b)//3,(a+b)*2//3
    c1,a1,b1=maxSum(n,a,m1)
    c2,a2,b2=maxSum(n,m1+1,m2)
    c3,a3,b3=maxSum(n,m2+1,b)
    if c1 < c2:c1,c2=c2,c1;a1,a2=a2,a1;b1,b2=b2,b1
    if c1 < c3:c1,c3=c3,c1;a1,b1=a3,b3
    return c1,a1,b1
n=list(map(int,input().split()))
print(maxSum(n,0,len(n)-1))
'''
def maxSum(n,a,b):
    if a==b:return n[a],a,b
    m=(a+b)//2
    c1,a1,b1=maxSum(n,a,m)
    c2,a2,b2=maxSum(n,m+1,b)
    print(c1, c2)
    if a2-b1==1:
        print(c1,c2)
        c3=c1+c2;a3=a1;b3=b2
        if c1 < c3:c1=c3;a1=a3;b1=b3
    if c1 < c2: c1 = c2;a1 = a2;b1 = b2

    return c1,a1,b1
n=list(map(int,input().split()))
print(maxSum(n,0,len(n)-1))
