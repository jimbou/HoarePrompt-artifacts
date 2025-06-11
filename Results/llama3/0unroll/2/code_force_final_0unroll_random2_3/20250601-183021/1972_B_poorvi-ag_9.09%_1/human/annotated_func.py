#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines: the first line contains a positive integer n (1 ≤ n ≤ 100), and the second line contains a string s of length n consisting only of "U" and "D".
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
        
    #State: Output State: The value of t is 0, results is a list of strings where each string is either 'yes' or 'no', and stdin is empty.
    for i in results:
        print(i)
        
    #State: Output State: The value of t is 0, results is a list of strings where each string is either 'yes' or 'no', and stdin is empty.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n and a string s of length n containing only "U" and "D". It then determines for each test case whether the string can be made valid by flipping some characters, and prints 'yes' if possible and 'no' otherwise. The function processes all test cases and prints the results in the order they were received.

