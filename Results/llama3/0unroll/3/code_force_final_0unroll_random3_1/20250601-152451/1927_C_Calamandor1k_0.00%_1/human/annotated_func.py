#State of the program right berfore the function call: stdin contains an integer t, followed by t test cases. Each test case contains three integers n, m, and k, followed by n integers a_1, a_2, ..., a_n, and m integers b_1, b_2, ..., b_m. n, m, and k are positive integers, 1 <= n, m <= 2*10^5, 2 <= k <= 2*min(n, m), and k is even. 1 <= a_i, b_j <= 10^6.
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        len_a, len_b = len(a), len(b)
        
        count_a, count_b = 0, 0
        
        d = k // 2
        
        for i in range(max(len_a, len_b)):
            if len_a > i + 1:
                if a[i] <= k:
                    count_a += 1
            if len_b > i + 1:
                if b[i] <= k:
                    count_b += 1
        
        print('YES' if count_a >= d and count_b >= d else 'NO')
        
    #State: Output State: The loop will print 'YES' or 'NO' for each test case, depending on whether the conditions count_a >= d and count_b >= d are met. The values of t, n, m, k, a, b, len_a, len_b, count_a, count_b, and d will be updated for each test case. The stdin will be empty after the loop finishes executing.

#Overall this is what the function does:This function reads input from standard input, processes multiple test cases, and prints 'YES' or 'NO' for each case. It takes no parameters and returns no value. The function's purpose is to determine whether two sequences of integers meet certain conditions based on their lengths and values. For each test case, it reads three integers (n, m, k) and two sequences of integers (a and b), then checks if the count of elements in each sequence that are less than or equal to k is greater than or equal to half of k. If both conditions are met, it prints 'YES'; otherwise, it prints 'NO'. The function processes all test cases and leaves the standard input empty after execution.

