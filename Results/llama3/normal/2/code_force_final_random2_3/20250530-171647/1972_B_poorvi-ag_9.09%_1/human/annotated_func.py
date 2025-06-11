#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 ≤ t ≤ 100) and then a string of length n (1 ≤ n ≤ 100) containing only "U" and "D".
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
        
    #State: t is an integer between 1 and 100 and is equal to 0, i is equal to t, n is an integer equal to the integer value of the last input, arr is a string equal to the second last input, stdin contains no test cases, results is a list containing 'no' if n is even for all iterations, otherwise results is a list containing 'yes' if arr has more 'U' characters than 'D' characters for all iterations, otherwise results is a list containing 'no'.
    for i in results:
        print(i)
        
    #State: `t` is an integer between 1 and 100 and is equal to 0, `i` is the last element in the list, `n` is an integer equal to the integer value of the last input, `arr` is a string equal to the second last input, `stdin` contains no test cases, `results` is a list that must have at least as many elements as the number of iterations of the loop, and the last element of the list which is `i` has been printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a string containing only "U" and "D" characters. It then determines for each test case whether the string has more "U" characters than "D" characters if the length of the string is odd, and prints "yes" if true, otherwise prints "no". If the length of the string is even, it always prints "no". The function continues this process until all test cases have been read from standard input.

