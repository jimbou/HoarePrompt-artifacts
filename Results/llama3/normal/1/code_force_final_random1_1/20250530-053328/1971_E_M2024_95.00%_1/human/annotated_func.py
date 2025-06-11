#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four lines of input. The first line contains three integers n, k, and q. The second and third lines contain k integers. The fourth line contains q integers. n and k are non-negative integers such that 1 <= k <= n <= 10^9 and 1 <= q <= 10^5. The sum of k over all test cases doesn't exceed 10^5, and the sum of q over all test cases doesn't exceed 10^5.
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
            m += bd[s] * ql / ad[s]
            print(int(m), end=' ')
        
        print()
        
    #State: t is 0, n is an integer, k is an integer, q is an integer and must be equal to 0, a is a list of at least k+1 integers, b is a list of at least len(b) integers, ad is a list containing len(a) integers: 0, a[1] - a[0], a[2] - a[1], ..., a[len(a) - 1] - a[len(a) - 2], bd is a list containing len(b) integers: 0, b[1] - b[0], b[2] - b[1], ..., b[len(b) - 1] - b[len(b) - 2], i is len(a) - 1, ql is an integer equal to the first input minus a[s - 1] minus a[s - 1] minus a[s - 1] ... minus a[s - 1] (q times), s is an integer representing the insertion point of ql in a to maintain sorted order, l is q-1, q is 0, nothing is being printed, _ is t-1, v is a list containing len(a) elements: 0, ad[1] / bd[1], ad[2] / bd[2], ..., ad[len(a) - 1] / bd[len(a) - 1], m is m plus b[s - 1] plus bd[s] times ql divided by ad[s] plus b[s - 1] plus bd[s] times ql divided by ad[s] plus b[s - 1] plus bd[s] times ql divided by ad[s] ... plus b[s - 1] plus bd[s] times ql divided by ad[s] (q times), and nothing is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of four lines of input. It processes each test case by calculating the differences between consecutive elements in the second and third lines of input, and then uses these differences to interpolate the corresponding values in the fourth line of input. The function prints the interpolated values for each test case, separated by spaces, and then prints a newline character to separate the output for each test case.

