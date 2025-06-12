#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n (1 <= n <= 10^6) and then a string s of length n consisting of lowercase Latin letters.
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
        
    #State: stdin is empty, t test cases have been processed, for each test case, the number of occurrences of 'map' or 'pie' in the string s with a sliding window of size 3 has been printed, and all substrings of length 3 from each string s have been printed.

#Overall this is what the function does:This function processes a series of test cases from standard input. For each test case, it reads an integer n and a string s of length n, then counts and prints the number of occurrences of the substrings 'map' or 'pie' in s using a sliding window of size 3. Additionally, it prints all substrings of length 3 from each string s. After processing all test cases, the function leaves the standard input empty.

