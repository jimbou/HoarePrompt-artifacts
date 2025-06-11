#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 10^3). Each test case contains a single integer n (3 <= n <= 10^5).
    for i in range(int(input())):
        n = [int(i) for i in input().split()][0]
        
        p = [0] * n
        
        ind = n
        
        for i in range(0, n, 2):
            p[i] = ind
            ind -= 2
        
        ind = 1 + n % 2
        
        for i in range(1, n, 2):
            p[i] = ind
            ind += 2
        
        print(*p)
        
    #State: The output state will contain t lines, each containing a sequence of n numbers. The numbers in each sequence will be arranged in a specific pattern, where the numbers at even indices will be decreasing from n, and the numbers at odd indices will be increasing from 1 (or 2 if n is even), with a step of 2. For example, if n = 5, the output will be "5 2 3 4 1". If n = 6, the output will be "6 4 5 2 3 1".

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a single integer n. It then generates a sequence of n numbers, arranging them in a specific pattern where numbers at even indices decrease from n and numbers at odd indices increase from 1 (or 2 if n is even) with a step of 2. The function prints each generated sequence on a new line, resulting in a total of t lines of output, where t is the number of test cases.

