#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first a positive integer (1 ≤ n ≤ 100) and then a string s of length n containing only "U" and "D".
    t = int(input())
    results = []
    for i in range(t):
        n = int(input())
        
        arr = input()
        
        if arr.count('U') % 2 == 1:
            results.append('yes')
        else:
            results.append('no')
        
    #State: Output State: The variable t is an integer equal to 0, results is a list of strings where each string is either 'yes' or 'no' depending on whether the count of 'U' in the corresponding test case string is odd or even respectively, and stdin is empty.
    for i in results:
        print(i)
        
    #State: Output State: The variable t is an integer equal to 0, results is a list of strings where each string is either 'yes' or 'no' depending on whether the count of 'U' in the corresponding test case string is odd or even respectively, and stdin is empty.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n and a string s of length n containing only "U" and "D". It then determines whether the count of 'U' in each string is odd or even and outputs 'yes' if it's odd and 'no' if it's even. The function processes all test cases and prints the results, one per line, until standard input is empty.

