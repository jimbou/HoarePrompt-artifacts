#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a sequence of integers (each representing the largest number Vladislav writes). The first integer is a positive integer and each of the following integers is a positive integer less than or equal to 2*10^5.
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: `t` is a positive integer, `values` is a list of 200001 integers where `values[i]` is equal to `values[i - 1]` plus the sum of all digits of `i`, `values[0]` to `values[199999]` are zeros, `values[200000]` is not zero, `stdin` contains a sequence of integers, `i` is at least 200000 and has at least 6 digits, `x` is the last digit of `i`, and `sum_value_digits` is equal to the sum of all digits of `i`.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: t is 0, values is a list of 200001 integers where values[i] is equal to values[i - 1] plus the sum of all digits of i, values[0] to values[199999] are zeros, values[200000] is not zero, stdin contains a sequence of integers, i is at least 200000 and has at least 6 digits, x is the last digit of i, sum_value_digits is equal to the sum of all digits of i, and value is the last integer read from the input sequence, and the value at index value in the values list is being printed, which is equal to values[value - 1] plus the sum of all digits of value.

#Overall this is what the function does:The function reads a sequence of integers from standard input, where the first integer represents the number of test cases, and each subsequent integer represents the largest number Vladislav writes. It then calculates the sum of digits for each number from 1 to 200000 and stores these sums in a list. For each test case, it prints the sum of digits for the given number. The function does not modify the input sequence or any external state, and its output is solely based on the input values.

