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
        
    #State: t is greater than or equal to 0, i is t-1, stdin is empty, n is an integer, arr is a string. If n is even, results is a list containing the string 'no' repeated t times. If n is odd, results is a list containing the string 'yes' if the number of 'U' characters in arr is greater than the number of 'D' characters, otherwise results is a list containing the string 'no' repeated t times.
    for i in results:
        print(i)
        
    #State: `t` is greater than or equal to 0, `i` is the last element in the `results` list, `stdin` is empty, `n` is an integer, `arr` is a string, `results` is not empty, and the last element in the `results` list which is `i` has been printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n and a string s of length n containing only "U" and "D" characters. It then determines for each test case whether the number of "U" characters is greater than the number of "D" characters if n is odd, and prints "yes" if true, otherwise prints "no". If n is even, it always prints "no". The function continues this process until all test cases have been read from standard input, at which point it has printed the results for all test cases.

