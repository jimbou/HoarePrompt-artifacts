#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[j for j in range(n)])
        
    #State: The output state contains t lines, each containing a sequence of integers. If k is 1, the sequence is a list of integers from 0 to n-1. If k is greater than 1 and equal to n, the sequence is a list of k repeated k times. If k is greater than 1 and not equal to n, the sequence is -1.

#Overall this is what the function does:The function reads input from standard input, where the first line contains an integer t, representing the number of test cases. Each subsequent line contains two integers, n and k, where n is the number of elements in a sequence and k is a parameter that determines the sequence's pattern. The function generates and prints t sequences, each based on the values of n and k. If k is 1, the sequence consists of integers from 0 to n-1. If k is greater than 1 and equal to n, the sequence consists of k repeated k times. If k is greater than 1 and not equal to n, the sequence is -1. The function prints each sequence on a separate line, resulting in t lines of output.

