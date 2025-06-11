#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a sequence of integers (the largest number Vladislav writes for each test case). The number of test cases is a positive integer and the largest number Vladislav writes for each test case is a positive integer less than or equal to 2 * 10^5.
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: values is a list of 2 * 10^5 + 1 integers, where each value at index i is the sum of the digits of all integers from 1 to i.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: The loop will execute t times, and for each iteration, it will print the sum of the digits of all integers from 1 to the input value. The values list will remain unchanged.

#Overall this is what the function does:The function reads a positive integer (the number of test cases) and a sequence of positive integers (the largest number Vladislav writes for each test case) from standard input, calculates the sum of the digits of all integers from 1 to each input value, and prints these sums. The function does not modify the input values or any external state, and its output is solely based on the input values.

