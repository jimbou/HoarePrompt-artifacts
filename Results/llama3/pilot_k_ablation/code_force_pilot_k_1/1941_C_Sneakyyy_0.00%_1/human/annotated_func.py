#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then a string s of length n. The integer t is a positive integer not greater than 10^4. The integer n is a positive integer not greater than 10^6. The sum of n over all test cases does not exceed 10^6. The string s consists of lowercase Latin letters.
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
        
    #State: stdin is empty, ans is not defined, i is not defined, a is not defined, t test cases have been processed, and the number of occurrences of 'map' or 'pie' in each test case string as substrings of length 3 have been printed.

#Overall this is what the function does:This function processes a series of test cases from standard input, where each test case consists of an integer n followed by a string s of length n. It counts and prints the number of occurrences of the substrings 'map' or 'pie' in each string, considering only substrings of length 3. After processing all test cases, the function leaves the standard input empty and does not return any value.

