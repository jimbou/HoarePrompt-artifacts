#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then a string s of length n. 1 <= t <= 10^4, 1 <= n <= 10^6, and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: _ is equal to the number of test cases, stdin is empty, and the number of non-overlapping occurrences of 'map' or 'pie' in the last test case string which is ans is being printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string s of length n. It then counts the number of non-overlapping occurrences of the substrings 'map' or 'pie' in each string and prints the count for each test case. The function processes all test cases and empties the standard input.

