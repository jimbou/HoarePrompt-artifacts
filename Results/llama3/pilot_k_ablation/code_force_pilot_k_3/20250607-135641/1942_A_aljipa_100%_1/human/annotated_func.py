#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(1, n + 1) if k == 1 else [-1]
        
        print(*res)
        
    #State: t is an integer between 1 and 10^3 (inclusive), stdin contains 0 lines, _ is t-1, n is an integer, k is an integer, res is a list of length n containing either all 1s, a range of integers from 1 to n, or all -1s, and the elements of the list res are being printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two integers n and k. It then generates a list of length n based on the values of n and k: if k equals n, the list contains all 1s; if k equals 1, the list contains a range of integers from 1 to n; otherwise, the list contains all -1s. Finally, it prints the generated list for each test case.

