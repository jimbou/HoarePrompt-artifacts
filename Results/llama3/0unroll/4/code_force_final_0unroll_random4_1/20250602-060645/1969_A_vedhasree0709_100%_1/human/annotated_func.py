#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            p = l[i]
            q = l[p - 1]
            if q == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: The output state contains t lines, each containing either 2 or 3. If a test case contains a pair of integers (p, q) such that q = p + 1, the output is 2. Otherwise, the output is 3.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of distinct integers. It checks each list for a specific condition: whether there exists a pair of integers (p, q) such that q = p + 1. If such a pair is found, it prints 2; otherwise, it prints 3. The function processes multiple test cases and outputs the result for each case.

