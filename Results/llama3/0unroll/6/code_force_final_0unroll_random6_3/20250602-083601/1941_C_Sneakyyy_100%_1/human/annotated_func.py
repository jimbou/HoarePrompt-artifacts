#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n (1 <= n <= 10^6) and then a string s of length n consisting of lowercase Latin letters.
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
        
    #State: The number of non-overlapping occurrences of 'map' or 'pie' in each string s, for each test case, printed on a new line.

#Overall this is what the function does:Counts and prints the number of non-overlapping occurrences of 'map' or 'pie' in each input string, for multiple test cases.

