#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first a positive integer (1 <= n <= 100) and then a string of length n containing only "U" and "D".
    t = int(input())
    results = []
    for i in range(t):
        n = int(input())
        
        arr = input()
        
        if arr.count('U') % 2 == 1:
            results.append('yes')
        else:
            results.append('no')
        
    #State: t is a positive integer, i is t-1, results is a list containing either 'yes' or 'no', n is a positive integer between 1 and 100, arr is a string of length n containing only "U" and "D", stdin contains no test cases. If the count of 'U' in arr is odd, results contains 'yes', otherwise results contains 'no'.
    for i in results:
        print(i)
        
    #State: The loop has finished executing, and all elements in the list `results` have been printed. The variable `i` now holds the value of the last element in the list `results`.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer (n) and a string of length n containing only "U" and "D". It then determines whether the count of 'U' in the string is odd or even and appends 'yes' or 'no' to a results list accordingly. Finally, it prints all elements in the results list.

