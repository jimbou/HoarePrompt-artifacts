#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 10^6) followed by a string s of length n consisting of lowercase Latin letters.
    for _ in range(int(input())):
        a = input()
        
        ans = 0
        
        i = 0
        
        while i < len(a) - 2:
            s = a[i:i + 3]
            print(s)
            if s == 'map' or s == 'pie':
                i += 3
                ans += 1
            else:
                i += 1
        
        print(ans)
        
    #State: `a` is the same string input from the user, `ans` is the number of non-overlapping occurrences of 'map' or 'pie' in `a`, `i` is `len(a)`, `_` is `t`, and `s` is the last substring of length 3 in `a` starting from index `len(a) - 3`, and the number of non-overlapping occurrences of 'map' or 'pie' in `a` which is equal to `ans` is being printed.

#Overall this is what the function does:Counts and prints the number of non-overlapping occurrences of the substrings 'map' or 'pie' in a given string for multiple test cases.

