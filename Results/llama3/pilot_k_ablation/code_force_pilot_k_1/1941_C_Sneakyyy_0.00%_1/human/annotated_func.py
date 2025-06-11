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
        
    #State: stdin contains 0 test cases, 'a' is the last test case, 'ans' is the number of times the substrings 'map' or 'pie' appear in the last test case consecutively, 'i' is equal to the length of the last test case - 2, and the number of times the substrings 'map' or 'pie' appear in each test case consecutively is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a string of lowercase Latin letters. It then counts the number of consecutive occurrences of the substrings 'map' or 'pie' in each test case and prints this count. The function processes all test cases and prints the count for each case. After execution, the function leaves the standard input empty and stores the last test case and its corresponding count in the variables 'a' and 'ans', respectively.

