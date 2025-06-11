#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[(j + 1) for j in range(n)])
        
    #State: The loop has finished executing, and the file object open(0) is exhausted. The output state is the same as the initial state, with the addition of the output of the loop for each iteration.

#Overall this is what the function does:This function reads input from standard input, where the first line contains an integer t, representing the number of test cases, followed by t lines, each containing two integers n and k. For each test case, if k is 1, it prints the numbers from 1 to n. If k is greater than or equal to 2, it checks if n is equal to k. If they are equal, it prints k repeated k times. If n is not equal to k, it prints -1. After processing all test cases, the function exhausts the file object and outputs the results of all iterations, leaving the output state as the initial state with the added output.

