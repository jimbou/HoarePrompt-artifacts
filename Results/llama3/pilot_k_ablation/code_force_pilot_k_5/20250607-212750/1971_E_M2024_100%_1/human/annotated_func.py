#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four lines of input. The first line contains three integers n, k, and q. The second and third lines contain k integers. The fourth line contains q integers. n, k, and q are non-negative integers such that 1 <= t <= 10^4, k <= n <= 10^9, and 1 <= k, q <= 10^5. The sum of k over all test cases doesn't exceed 10^5, and the sum of q over all test cases doesn't exceed 10^5.
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
        
    #State: t is a non-negative integer such that 0 <= t <= 10^4, _ is t, n is an integer, k is at least 1 and less than the length of a, q is an integer, a is a list of at least len(a) integers, b is a list of at least len(b) integers, ad is a list containing len(a) integers 0, a[1] - a[0], a[2] - a[1], ..., a[len(a) - 1] - a[len(a) - 2], bd is a list containing len(b) integers 0, b[1] - b[0], b[2] - b[1], ..., b[len(b) - 1] - b[len(b) - 2], v is a list containing len(a) integers 0, ad[1] / bd[1], ad[2] / bd[2], ..., ad[len(a) - 1] / bd[len(a) - 1], i is len(a) - 1, l is q, ql is an integer equal to the input minus a[s-1], m is m plus b[s-1] plus the integer division of bd[s] times ql by ad[s], s is an integer such that a[s-1] < ql <= a[s], nothing is printed, stdin contains 0 inputs, and an empty line is printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of four lines of input. It then processes the input data, calculates intermediate values, and prints the results for each test case. The function takes no arguments and returns no value. Its purpose is to solve a specific problem by performing calculations based on the input data and printing the results in a specific format.

