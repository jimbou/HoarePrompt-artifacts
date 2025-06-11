#State of the program right berfore the function call: stdin contains two inputs: first two space-separated integers n and k, then a space-separated list of n integers, and then a space-separated list of n integers. n is a positive integer, k is a non-negative integer, and the integers in the lists are non-negative integers.
    try:
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = [0] * (n + 1)
        for i in range(n):
            x = int(input())
            
            b[abs(x)] += a[i]
            
        #State: Output State: n is a positive integer, k is a non-negative integer, a is a list of n non-negative integers, b is a list of n+1 integers where the value at index i is the sum of the ith element of a and the absolute value of the ith integer from the input.
        r = 0
        for i in range(1, n + 1):
            r += k
            
            if r < b[i]:
                print('NO')
                return
            
            r -= b[i]
            
        #State: Output State: r is the sum of the differences between k and the sum of the ith element of a and the absolute value of the ith integer from the input, for all i from 1 to n, a is a list of n non-negative integers, b is a list of n+1 integers where the value at index i is the sum of the ith element of a and the absolute value of the ith integer from the input, n is a positive integer, k is a non-negative integer.
        print('YES')
        #This is printed: YES
    except (ValueError):
        print('Invalid input format')
        #This is printed: Invalid input format
    #State: `n` is a positive integer, `k` is a non-negative integer, `a` is a list of `n` non-negative integers, `b` is a list of `n+1` integers where the value at index `i` is the sum of the `i`th element of `a` and the absolute value of the `i`th integer from the input, and either 'YES' or 'NO' is printed, or 'Invalid input format' is printed if the input is invalid.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints either 'YES', 'NO', or 'Invalid input format'. It accepts no parameters and returns no value. The function's purpose is to determine whether a given condition is met based on the input values. If the input is valid, it checks if a cumulative sum of differences between a given value `k` and sums of pairs of input integers is non-negative. If this condition is met, it prints 'YES'; otherwise, it prints 'NO'. If the input is invalid, it prints 'Invalid input format'.

#State of the program right berfore the function call: stdin contains one input: an integer (t) representing the number of test cases.
    try:
        t = int(input())
        for _ in range(t):
            func_1()
            
        #State: Output State: `t` is an integer representing the number of test cases, stdin is empty.
    except (ValueError):
        print('Invalid input format')
        #This is printed: Invalid input format
    #State: `t` is an integer representing the number of test cases if the input is valid, otherwise, the state is unknown, and 'Invalid input format' is printed.

#Overall this is what the function does:Reads an integer from standard input representing the number of test cases, then calls another function (`func_1`) that number of times. If the input is not a valid integer, it prints an error message and does not perform any further actions.

