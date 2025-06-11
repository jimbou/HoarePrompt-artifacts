#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t binary strings s (2 <= |s| <= 2 * 10^5; s_i in {0, 1}).
    n = int(input())
    for _ in range(n):
        s = list(map(int, input().strip()))
        
        zeroes = s.count(0)
        
        cnt = [0, 0]
        
        ans = 0
        
        for c in s:
            cnt[c] += 1
            if c == 0:
                ans += 1 if cnt[1] > 0 else 0
            else:
                ans += zeroes - cnt[0]
        
        print(ans)
        
    #State: The loop will have printed the total number of operations required to make all the binary strings alternating between 0s and 1s, for each of the n input strings. The value of n will be unchanged, and the stdin will be empty after reading all the input strings.

#Overall this is what the function does:This function reads an integer n from standard input, followed by n binary strings. It then calculates and prints the minimum number of operations required to make each binary string alternating between 0s and 1s. The function processes all input strings and prints the result for each string, leaving the standard input empty after reading all input strings.

