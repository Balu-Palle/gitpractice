for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[]
    dp=[]
    for i in range(n):
        l1=[0]*(m)
        l=list(map(int,input().split()))
        dp.append(l1)
        a.append(l)
    dp[0][0]=a[0][0]
    for i in range(1,m):
        dp[0][i]=dp[0][i-1]+a[0][i]
    for j in range(1,n):
        # print(dp)
        dp[j][0]=dp[j-1][0]+a[j][0]
    
    
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])+a[i][j]
    # print(dp)
    print(dp[n-1][m-1])

