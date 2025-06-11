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
        
    #State: `s` is an empty list, `c` is undefined, `zeroes` is the count of zeroes in the original list `s`, `n` is 0, `_` is `n`, `cnt` is a list with two elements where the first element is the count of zeroes in the original list `s` and the second element is the count of ones in the original list `s`, and `ans` is the sum of the counts of zeroes in the original list `s` minus the count of zeroes in the original list `s` plus the count of ones in the original list `s` if the count of ones in the original list `s` is greater than 0, otherwise `ans` is the count of zeroes in the original list `s`.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t binary strings. For each binary string, it calculates the sum of the counts of zeroes minus the count of zeroes plus the count of ones if the count of ones is greater than 0, otherwise it calculates the count of zeroes. The function then prints the calculated sum for each binary string.

