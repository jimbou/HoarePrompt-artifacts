#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 10^3) followed by t lines, each containing two integers x (1 ≤ x ≤ 10^8) and n (1 ≤ n ≤ x).
    for q in range(int(input())):
        x, n = list(map(int, input().split(' ')))
        
        ans = 1
        
        for i in range(1, int(sqrt(x)) + 1):
            if x % i == 0:
                if x - n * i >= 0 and (x - n * i) % i == 0:
                    ans = max(ans, i)
                if x - n * (x // i) >= 0 and x // i > 0 and x - n * (x // i) % (x // i
                    ) == 0:
                    ans = max(ans, x // i)
        
        print(ans)
        
    #State: stdin is empty, q is equal to the initial value of t, x and n are undefined, ans is undefined, and the maximum divisor i of each x such that x - n * i >= 0 and (x - n * i) % i == 0 or x - n * (x // i) >= 0 and x // i > 0 and (x - n * (x // i)) % (x // i) == 0 has been printed for each pair of x and n.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, where each pair represents a number x and a multiplier n. For each pair, it calculates and prints the maximum divisor i of x such that x - n * i is non-negative and divisible by i, or x - n * (x // i) is non-negative, x // i is positive, and divisible by x // i. The function processes all input pairs and prints the maximum divisor for each pair, leaving the input stream empty after execution.

