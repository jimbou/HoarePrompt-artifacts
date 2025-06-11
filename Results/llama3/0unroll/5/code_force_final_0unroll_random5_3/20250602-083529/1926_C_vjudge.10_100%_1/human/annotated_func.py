#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a list of integers (the largest number Vladislav writes for each test case). The first integer is a positive integer and the integers in the list are positive integers less than or equal to 2 * 10^5.
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: Output State: The loop will run indefinitely because the range is set to infinity. The values list will continue to grow indefinitely, with each index i being the sum of the digits of i plus the value at index i-1. The sum_value_digits variable will continue to calculate the sum of the digits of each number i. The variable i will continue to increment indefinitely.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: Output State: The loop will run for a finite number of iterations, equal to the value of t. The values list will be accessed and printed at the index equal to the input value, for each iteration. The variable i will not be used in the loop body, and the sum_value_digits variable will not be used or updated in the loop.

#Overall this is what the function does:This function reads a positive integer (the number of test cases) and a list of integers (the largest number Vladislav writes for each test case) from standard input, calculates the cumulative sum of digits for numbers up to 2 * 10^5, and then prints the cumulative sum of digits for each input number.

