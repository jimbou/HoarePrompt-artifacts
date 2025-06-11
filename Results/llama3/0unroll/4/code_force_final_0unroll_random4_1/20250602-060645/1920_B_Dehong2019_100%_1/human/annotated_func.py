#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers n, k, and x. The second line contains n integers a_1, a_2,\ldots,a_n. 1 <= n <= 2 * 10^5, 1 <= x, k <= n, 1 <= a_i <= 1000.
    """
    Created on Fri Sep  6 21:42:15 2024
     
    @author: dehon
    """
    t = int(input())
    for _ in range(t):
        n, k, x = map(int, input().split())
        
        a = sorted(list(map(int, input().split())), reverse=True)
        
        ans1 = sum(a)
        
        for i in range(x):
            ans1 -= a[i] * 2
        
        ans2 = ans1
        
        for i in range(k):
            ans1 += a[i]
            if i + x < n:
                ans1 -= a[i + x] * 2
            ans2 = max(ans1, ans2)
        
        print(ans2)
        
    #State: The loop has executed t times, and for each execution, it has read two lines from stdin, processed the input, and printed the maximum value of ans2. The value of t has not changed, but stdin has been consumed by t - 1 test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains three integers (n, k, and x) and the second line contains n integers. It processes each test case by sorting the integers in descending order, calculating a maximum value (ans2) based on a series of operations involving the integers, k, and x, and prints the maximum value for each test case. After processing all test cases, the function concludes, having consumed the corresponding number of lines from standard input.

