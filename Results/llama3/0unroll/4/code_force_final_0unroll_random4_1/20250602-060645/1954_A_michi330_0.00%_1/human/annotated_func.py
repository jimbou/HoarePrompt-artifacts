#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 1000) followed by t lines, each containing three integers n, m, and k (1 <= m, k <= n <= 50).
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: The output will be a series of 'YES' or 'NO' printed to the console, with each line corresponding to the input provided in the stdin. The number of lines will be equal to the value of 't'.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers: n, m, and k. It then determines whether it is possible to satisfy a certain condition based on these values, printing 'YES' if possible and 'NO' otherwise. The function repeats this process for each test case provided in the input, printing a corresponding 'YES' or 'NO' for each case.

