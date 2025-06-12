#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four lines. The first line contains three integers n, k, and q. The second and third lines contain k integers. The fourth line contains q integers. n and k are positive integers such that k <= n. q is a positive integer. The sum of k over all test cases doesn't exceed 10^5, and the sum of q over all test cases doesn't exceed 10^5.
    t = int(input())
    for _ in range(t):
        n, k, q = map(int, input().split())
        
        a = [0] + list(map(int, input().split()))
        
        b = [0] + list(map(int, input().split()))
        
        ad = [0]
        
        bd = [0]
        
        for i in range(1, len(a)):
            ad.append(a[i] - a[i - 1])
        
        for i in range(1, len(b)):
            bd.append(b[i] - b[i - 1])
        
        v = [0]
        
        for i in range(1, len(a)):
            v.append(ad[i] / bd[i])
        
        for l in range(q):
            m = 0
            i = 1
            ql = int(input())
            s = bisect_left(a, ql)
            if a[s] == ql:
                print(b[s], end=' ')
                continue
            ql -= a[s - 1]
            m += b[s - 1]
            m += bd[s] * ql // ad[s]
            print(m, end=' ')
        
        print()
        
    #State: `t` is 0, stdin contains no more test cases, all other variables are undefined or have their initial values (before the loop execution).

#Overall this is what the function does:This function reads multiple test cases from standard input, each consisting of four lines, and for each test case, it calculates and prints the interpolated values of a function defined by two sets of points (a and b) at given query points (q). The function assumes that the input points in a and b are sorted in ascending order and that the query points are within the range of the input points. After processing all test cases, the function leaves the input stream empty and all variables are reset to their initial state.

