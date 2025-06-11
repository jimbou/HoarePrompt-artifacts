#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains two integers n and m (1 ≤ n ≤ m ≤ 2 × 10^5). The second line contains n integers a_i (1 ≤ a_i ≤ 10^9). The third line contains m integers b_i (1 ≤ b_i ≤ 10^9).
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
        
    #State: m is an integer, n is 0, i is equal to the initial value of n, a is an empty list, b is an empty list, result is a list containing the absolute differences between the maximum value in the original list a and the minimum value in the original list b, stdin contains no more test cases, and the sum of the absolute differences between the maximum value in a and the minimum value in b is printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two lists of integers. It calculates the absolute differences between the maximum value in the first list and the minimum value in the second list, and prints the sum of these differences. The function continues this process until all test cases have been read from standard input.

