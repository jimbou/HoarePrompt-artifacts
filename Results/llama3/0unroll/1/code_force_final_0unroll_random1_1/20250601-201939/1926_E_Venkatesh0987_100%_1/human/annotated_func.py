#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5 * 10^4) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^9).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        s = 0
        
        i = 0
        
        d = n
        
        h = n
        
        p = 1
        
        g = 0
        
        if k > (n + 1) // 2:
            while s < k and d > 0:
                s += (d + 1) // 2
                d -= (d + 1) // 2
                i += 1
            while p <= i - 1:
                g += (h + 1) // 2
                h -= (h + 1) // 2
                p += 1
            f = k - g
            y = 2 ** (i - 1) * (2 * f - 1)
            print(y)
        else:
            print(2 * k - 1)
        
    #State: The output state is a list of integers, each representing the result of the calculation for the corresponding input pair (n, k). The list has a length of t, where t is the number of input pairs. Each integer in the list is either 2*k - 1 (if k <= (n + 1) // 2) or 2^(i - 1) * (2*f - 1) (if k > (n + 1) // 2), where i is the number of iterations of the while loop and f is the difference between k and the sum of the first i - 1 terms of the sequence h + 1 // 2.

#Overall this is what the function does:This function calculates and prints the result of a mathematical operation for each input pair (n, k), where n and k are integers. For each pair, if k is less than or equal to half of n, it prints 2*k - 1. Otherwise, it calculates the result using a while loop and prints 2^(i - 1) * (2*f - 1), where i is the number of iterations and f is the difference between k and the sum of the first i - 1 terms of a sequence. The function processes multiple input pairs and prints the results in a list.

