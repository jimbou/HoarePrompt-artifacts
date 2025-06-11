#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 10^3) and then t pairs of integers n and k (1 <= k <= n <= 10^3).
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[(j + 1) for j in range(n)])
        
    #State: The output state will contain t lines, each representing the result of the corresponding pair of integers n and k. If k is 1, the line will contain the numbers from 1 to n. If k is greater than 1 and n is equal to k, the line will contain k repeated k times. If k is greater than 1 and n is not equal to k, the line will contain -1.

#Overall this is what the function does:This function generates a sequence of numbers based on the input pairs of integers n and k. If k is 1, it outputs the numbers from 1 to n. If k is greater than 1 and n is equal to k, it outputs k repeated k times. If k is greater than 1 and n is not equal to k, it outputs -1. The function processes multiple pairs of integers and outputs the corresponding results in separate lines.

