#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a binary string of the same length as the integer. The integer is a positive integer less than or equal to 50.
    t = int(input())
    results = []
    for i in range(t):
        n = int(input())
        
        arr = input()
        
        if arr.count('1') == 2 and '11' in arr:
            results.append('no')
        
        if arr.count('1') % 2 == 0:
            if arr.count('1') == 2 and '11' in arr:
                results.append('no')
            else:
                results.append('yes')
        else:
            results.append('no')
        
    #State: Output State: t is a positive integer less than or equal to 50, results is a list containing 'yes' or 'no' for each test case, stdin contains no test cases.
    for r in results:
        print(r)
        
    #State: Output State: t is a positive integer less than or equal to 50, results is an empty list, stdin contains no test cases.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a positive integer (n) and a binary string of the same length as n. It then determines whether the binary string can be rearranged to have all '1's at even indices and all '0's at odd indices. If possible, it outputs 'yes' for that test case; otherwise, it outputs 'no'. The function processes all test cases and prints the results, one per line, before exiting.

