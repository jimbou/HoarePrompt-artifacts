#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers x (1 <= x <= 10^8) and n (1 <= n <= x).
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        k = x // n
        
        if k == 1:
            print(1)
            continue
        
        ans = 1
        
        for i in range(1 + (1 if x % 2 == 0 else 0), int(x ** 0.5) + 1, 2):
            if x % i == 0:
                l = [ans]
                if i <= k:
                    l.append(i)
                if x // i <= k:
                    l.append(x // i)
                ans = max(l)
        
        print(ans)
        
    #State: The final output state is the maximum value of `ans` after all iterations of the loop, where `ans` is the maximum value of `ans`, `i`, and `x` divided by `i` if `x` divided by `i` is less than or equal to `k`, or the maximum value of `ans` and `x` divided by `i` otherwise, and `i` is an odd integer between 1 + (1 if x % 2 == 0 else 0) and the square root of `x` (inclusive).

#Overall this is what the function does:This function reads a series of input pairs (x, n) from standard input, where x is an integer and n is a divisor of x. For each pair, it calculates and prints the maximum divisor of x that is less than or equal to x divided by n. If x is 1, it simply prints 1. The function iterates over all input pairs and outputs the maximum divisor for each pair.

