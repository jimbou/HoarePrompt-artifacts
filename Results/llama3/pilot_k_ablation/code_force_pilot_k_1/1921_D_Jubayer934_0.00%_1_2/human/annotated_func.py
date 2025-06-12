#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains two integers n and m (1 <= n <= m <= 2 * 10^5). The second line contains n integers a_i (1 <= a_i <= 10^9). The third line contains m integers b_i (1 <= b_i <= 10^9). The sum of m over all test cases does not exceed 2 * 10^5.
    n = int(input())
    for i in range(n):
        m, n = map(int, input().split())
        
        a = list(map(int, input().split()))[:m]
        
        b = list(map(int, input().split()))[:n]
        
        b.sort()
        
        result = []
        
        n = n // 2
        
        for i in range(len(a)):
            if len(a) == len(b):
                break
            b.remove(b[n - 1])
        
        for i in range(len(a)):
            result.append(abs(max(a) - min(b)))
            a.remove(max(a))
            b.remove(min(b))
        
        print(sum(result))
        
    #State: `n` is an integer between 1 and 2 * 10^5 inclusive, `i` is `n`, `a` is an empty list, `b` is an empty list, `result` is an empty list, and the sum of the absolute differences between the maximum value of each test case's `a` and the minimum value of each test case's `b` at each iteration has been printed for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains two lists of integers, `a` and `b`. It then calculates the sum of the absolute differences between the maximum value of `a` and the minimum value of `b` at each iteration, after removing the maximum value from `a` and the minimum value from `b` in each iteration, until `a` and `b` are empty. The function prints the sum of these absolute differences for each test case.

