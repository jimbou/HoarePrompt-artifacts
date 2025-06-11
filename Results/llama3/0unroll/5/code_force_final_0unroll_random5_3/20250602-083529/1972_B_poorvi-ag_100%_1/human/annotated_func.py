#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 100) followed by t test cases. Each test case contains an integer n (1 ≤ n ≤ 100) followed by a string s of length n containing only "U" and "D".
    t = int(input())
    results = []
    for i in range(t):
        n = int(input())
        
        arr = input()
        
        if arr.count('U') % 2 == 1:
            results.append('yes')
        else:
            results.append('no')
        
    #State: Output State: t is an integer between 1 and 100, results is a list of length t containing t strings, each of which is either 'yes' or 'no', stdin contains 0 inputs.
    for i in results:
        print(i)
        
    #State: Output State: t is an integer between 1 and 100, results is a list of length t containing t strings, each of which is either 'yes' or 'no', stdin contains 0 inputs, stdout contains t lines, each of which is either 'yes' or 'no'.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string s of length n containing only "U" and "D". It then determines whether the number of "U"s in each string is odd or even and outputs "yes" if it's odd and "no" if it's even, one output per test case.

