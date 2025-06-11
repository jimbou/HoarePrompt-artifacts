#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 10^6) followed by a string s of length n consisting of lowercase Latin letters.
    for _ in range(int(input())):
        n = int(input())
        
        a = input()
        
        ans = 0
        
        i = 0
        
        while i < len(a) - 2:
            s = a[i:i + 3]
            if s == 'map' or s == 'pie':
                i += 3
                ans += 1
            else:
                i += 1
        
        print(ans)
        
    #State: The loop variable `_` is equal to the integer `t` provided in the initial state, `n` is an integer greater than or equal to 0, `a` is a string, `ans` is the number of occurrences of 'map' or 'pie' in `a`, `i` is equal to the length of `a`, and `stdin` is empty, and the number of occurrences of 'map' or 'pie' in `a` which is `ans` is being printed.

#Overall this is what the function does:Counts and prints the number of occurrences of the substrings 'map' and 'pie' in a given string for multiple test cases.

