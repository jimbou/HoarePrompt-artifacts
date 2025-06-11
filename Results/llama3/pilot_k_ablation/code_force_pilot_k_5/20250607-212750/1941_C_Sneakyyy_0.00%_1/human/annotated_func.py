#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n (1 <= n <= 10^6) and then a string s of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
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
        
    #State: `stdin` is empty, `_` is `t`, `a` is an empty string, `i` is 0, `ans` is the total number of occurrences of 'map' or 'pie' in all test cases, and the total number of occurrences of 'map' or 'pie' in all test cases which is `ans` is being printed.

#Overall this is what the function does:Counts and prints the total number of occurrences of the substrings 'map' and 'pie' in all test cases provided through standard input.

