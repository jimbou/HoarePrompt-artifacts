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
        
    #State: The output state contains t lines, each representing the number of occurrences of the substrings 'map' or 'pie' in the corresponding input string.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string s of length n. It then counts the number of occurrences of the substrings 'map' and 'pie' in each string, and prints the count for each test case. The function does not modify the input strings or store any results beyond printing the counts.

