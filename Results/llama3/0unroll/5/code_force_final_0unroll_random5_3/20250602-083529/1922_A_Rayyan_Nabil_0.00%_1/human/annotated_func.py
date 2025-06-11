#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 20) followed by three strings a, b, and c, each of length n consisting of lowercase Latin letters.
    t = int(input())
    l = 'YES'
    for i in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        c = input()
        
        for i in range(n):
            if a[i] != c[i] and b[i] != c[i]:
                l = 'YES'
        else:
            l = 'NO'
        
        print(l)
        
    #State: Output State: The variable l is set to 'NO' if for all test cases, there exists at least one position where the characters in strings a and b are the same as the character in string c. Otherwise, l is set to 'YES'. The variable t is unchanged, still an integer between 1 and 1000 inclusive.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints a result for each case. It takes no parameters and returns no value. The function iterates over each test case, comparing characters in three input strings (a, b, and c) at corresponding positions. If it finds a position where characters in both a and b differ from the character in c, it sets a flag (l) to 'YES'. If no such position is found after checking all characters, the flag is set to 'NO'. The function then prints the flag value for each test case. The input variable t, representing the number of test cases, remains unchanged.

