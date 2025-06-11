#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing a binary string s (2 <= |s| <= 2 * 10^5).
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
        
    #State: `n` is 0, `_` is n, stdin is empty, `s` is an empty list, `zeroes` is the count of 0s in the last binary string from stdin, `cnt` is a list of two integers where the first element is the count of 0s in the last binary string from stdin and the second element is the count of 1s in the last binary string from stdin, `ans` is the sum of the counts of 1s in all the substrings of the last binary string from stdin that start with a 1 and end with a 0, and `c` is the last element in the last binary string from stdin.

#Overall this is what the function does:This function reads a series of binary strings from standard input, calculates the sum of the counts of 1s in all substrings that start with a 1 and end with a 0 for each string, and prints these sums. It processes multiple strings as specified by an initial integer input, and it exhausts the input stream in the process.

