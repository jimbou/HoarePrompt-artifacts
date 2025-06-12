#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four lines of input. The first line contains three integers n, k, and q. The second and third lines contain k integers. The fourth line contains q integers.
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
        
    #State: t is 0, stdin is empty, all other variables are undefined or have their initial values.

#Overall this is what the function does:The function reads multiple test cases from standard input, each containing four lines of input. It processes each test case by calculating the differences between consecutive elements in two lists, then uses these differences to calculate a new list of values. For each query in the test case, it finds the corresponding value in the new list and prints it. After processing all test cases, the function leaves the standard input empty and resets all variables to their initial values.

