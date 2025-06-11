#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: The output will be a series of lines, each containing a sequence of integers. For each input line, if k equals n, the output will be a sequence of 1s of length n. If k equals 1, the output will be a sequence of integers from 0 to n-1. For all other cases, the output will be a single -1. The number of output lines will be equal to the initial value of t.

#Overall this is what the function does:The function reads a series of input lines, each containing two integers n and k, and generates a corresponding output sequence for each line. If k equals n, the output sequence consists of 1s of length n. If k equals 1, the output sequence consists of integers from 0 to n-1. For all other cases, the output sequence is a single -1. The function prints these output sequences, with the number of output lines equal to the initial input value t.

