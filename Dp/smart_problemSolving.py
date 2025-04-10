def solve(dp,m,i,n):
    if (i>=n):
        return 0
    if dp[i]!=0:
        return dp[i]



    dp[i]=max((m[i][0]+solve(dp,m,i+1+m[i][1],n)),solve(dp,m,i+1,n))
    return dp[i]


for _ in range(int(input())):
    n=int(input())
    dp=[0]*(n+1)
    m=[]
    for i in range(n):
        
        a=list(map(int,input().split()))
        m.append(a)
        
    print(solve(dp,m,0,n))
    
    



        
        
        