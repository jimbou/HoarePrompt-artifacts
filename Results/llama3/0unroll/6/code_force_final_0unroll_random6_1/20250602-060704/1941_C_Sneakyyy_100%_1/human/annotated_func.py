#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then a string s of length n. 1 <= t <= 10^4 and 1 <= n <= 10^6. The sum of n over all test cases does not exceed 10^6.
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
        
    #State: The output state will contain t lines, each representing the count of non-overlapping occurrences of the substrings 'map' and 'pie' in the corresponding input string s. The count is calculated by iterating through the string and incrementing the count whenever 'map' or 'pie' is found, and moving the index forward by 3 characters in such cases, otherwise moving the index forward by 1 character.

#Overall this is what the function does:Counts and prints the number of non-overlapping occurrences of the substrings 'map' and 'pie' in a given string for multiple test cases.

