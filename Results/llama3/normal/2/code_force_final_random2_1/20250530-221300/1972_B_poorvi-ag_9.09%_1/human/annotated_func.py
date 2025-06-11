#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first a positive integer n (1 ≤ n ≤ 100) and then a string s of length n containing only "U" and "D".
    t = int(input())
    results = []
    for i in range(t):
        n = int(input())
        
        arr = input()
        
        if n % 2 == 0:
            results.append('no')
        elif arr.count('U') > arr.count('D'):
            results.append('yes')
        else:
            results.append('no')
        
    #State: t is 0, i is t, n is an integer, arr is a string, stdin is empty. If all n values are even, results is a list containing t strings 'no'. If any n value is odd, results is a list containing 'yes' for each n value that has more occurrences of 'U' than 'D' and 'no' for each n value that has less or equal occurrences of 'U' than 'D'.
    for i in results:
        print(i)
        
    #State: t is 0, i is the last element of results, n is an integer, arr is a string, stdin is empty, results is a list containing either 'yes' or 'no' for each n value, and the last element of the list results which is either 'yes' or 'no' has been printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n and a string s of length n containing only "U" and "D". It then determines for each test case whether the number of "U"s is greater than the number of "D"s when n is odd, and prints "yes" if true, otherwise "no". If all n values are even, it prints "no" for each test case. The function processes all test cases and prints the results in the order they were received.

