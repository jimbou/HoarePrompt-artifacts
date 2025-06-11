#State of the program right berfore the function call: stdin contains two inputs: first an integer and then a binary string. The integer is a positive integer and the binary string consists of only 0-s and/or 1-s.
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
        
    #State: `n` is 0, `_` is `n`, `s` is an empty list, `zeroes` is the number of zeroes in the list `s`, `cnt` is a list containing two integers where the first integer is equal to `zeroes` and the second integer is equal to the number of non-zero integers in `s`, `stdin` is empty, and `ans` is equal to the number of non-zero integers in `s` times `zeroes` minus the number of zeroes in `s` plus the number of non-zero integers in `s` that are equal to 1.

#Overall this is what the function does:The function reads a positive integer 'n' from standard input, followed by 'n' binary strings. For each binary string, it calculates and prints the number of pairs of adjacent 0s and 1s. After processing all 'n' binary strings, the function leaves the input stream empty and does not return any value.

