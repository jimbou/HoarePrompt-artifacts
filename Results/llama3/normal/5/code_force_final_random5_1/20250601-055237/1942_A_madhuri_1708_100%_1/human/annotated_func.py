#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^3), representing the number of test cases. Each of the following t lines contains two integers n and k (1 <= k <= n <= 10^3), representing the length of the array and the number of sorted cyclic shifts the array must have.
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[(j + 1) for j in range(n)])
        
    #State: The loop has executed for all test cases. For each test case, if k is greater than or equal to 2, then if n equals k, a list of k elements, all of which are equal to k, has been printed. Otherwise, -1 has been printed. If k is less than 2, a list of integers from 1 to n (inclusive) has been printed.

#Overall this is what the function does:The function reads input from standard input, processes multiple test cases, and prints the results. For each test case, it takes two integers n and k as input, representing the length of an array and the number of sorted cyclic shifts. If k is greater than or equal to 2, it checks if n equals k. If true, it prints a list of k elements, all equal to k. If false, it prints -1. If k is less than 2, it prints a list of integers from 1 to n (inclusive). The function continues this process until all test cases have been processed.

