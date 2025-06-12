#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains two integers n and m (1 ≤ n ≤ m ≤ 2 * 10^5). The second line contains n integers a_i (1 ≤ a_i ≤ 10^9). The third line contains m integers b_i (1 ≤ b_i ≤ 10^9).
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
        
    #State: `n` is 0, `i` is the initial value of `n`, `m` is the last value of `m` read from the input, `a` is an empty list, `b` is an empty list, `result` is not defined, and the sum of the absolute differences between the maximum values in `a` and the minimum values in `b` for each iteration of the loop has been printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two integers m and n, followed by m integers a_i and n integers b_i. It then calculates the sum of the absolute differences between the maximum values in a_i and the minimum values in b_i for each iteration of the loop, after removing the middle elements of b_i. The function prints the sum of these absolute differences for each test case.

