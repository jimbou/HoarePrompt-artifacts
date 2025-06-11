#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 10^3) followed by t lines, each containing two integers x (1 ≤ x ≤ 10^8) and n (1 ≤ n ≤ x).
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
        
    #State: The loop has finished executing, and the maximum value of `ans` has been printed for each iteration. The values of `x`, `n`, `k`, `i`, and `l` have been updated accordingly for each iteration. The loop has executed a total of `t` times, where `t` is the integer input at the beginning of the program.

#Overall this is what the function does:This function reads a series of input pairs (x, n) from standard input, where x and n are integers, and for each pair, it calculates and prints the maximum divisor of x that is less than or equal to n. The function repeats this process for a number of times specified by an initial integer input t.

