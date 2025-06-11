#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t binary strings s (2 <= |s| <= 2 * 10^5).
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
        
    #State: The output state will be the sum of the number of 1s in the binary string s that are preceded by at least one 0, plus the number of 0s in the binary string s that are followed by at least one 1, for each of the t binary strings s.

#Overall this is what the function does:This function reads a series of binary strings from standard input, where the number of strings is specified by an initial integer. For each binary string, it calculates and prints the sum of two counts: the number of 1s that are immediately preceded by at least one 0, and the number of 0s that are immediately followed by at least one 1. The function processes each string independently and outputs the calculated sums for each string.

