#State of the program right berfore the function call: stdin contains two inputs: first an integer (greater than 0 and less or equal than 10^4) and then a sequence of integers (each greater than 0 and less or equal than 2*10^5).
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: `stdin` contains 1 input: a sequence of integers, `inf` is 200001, `t` is an integer between 1 and 10^4 (inclusive), `values` is a list of 200001 integers where `values[i]` is the sum of all digits of `i` plus the sum of all digits of `i` from the previous iterations plus `values[i - 1]`, `i` is an integer with at least `inf` digits, `sum_value_digits` is equal to the sum of the digit `x` of `i` and the previous value of `sum_value_digits` plus the digit `x` of `i`, and `x` is the last digit of `i`.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: `inf` is 200001, `t` is 0, `values` is a list of 200001 integers where `values[i]` is the sum of all digits of `i` plus the sum of all digits of `i` from the previous iterations plus `values[i - 1]`, `i` is an integer with at least `inf` digits, `sum_value_digits` is equal to the sum of the digit `x` of `i` and the previous value of `sum_value_digits` plus the digit `x` of `i`, `x` is the last digit of `i`, and `value` is an integer input from stdin, stdin contains no input, and the value at index `value` in the `values` list which is the sum of all digits of `value` plus the sum of all digits of `value` from the previous iterations plus `values[value - 1]` is being printed, and `value` is assigned the value `int(input())`, where `input()` accepts an integer from stdin, and the value at index `value` in the `values` list which is the sum of all digits of `value` plus the sum of all digits of `value` from the previous iterations plus `values[value - 1]` is being printed.

#Overall this is what the function does:This function reads a sequence of integers from standard input, calculates the cumulative sum of digits for each integer from 1 to 200000, and then prints the cumulative sum of digits for each input integer. The function does not return any value but prints the results to standard output.

