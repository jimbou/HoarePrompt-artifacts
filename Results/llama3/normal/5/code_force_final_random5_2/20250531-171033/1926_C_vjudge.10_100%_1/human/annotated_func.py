#State of the program right berfore the function call: stdin contains two inputs: first an integer (greater than 0 and less than or equal to 10^4) and then a series of integers (each greater than 0 and less than or equal to 2 * 10^5) equal in number to the first integer.
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: `t` is an integer greater than 0 and less than or equal to 10^4, `values` is a list of 2 * 10^5 + 1 integers where `values[i]` is the sum of all digits of `i` plus `values[i - 1]`, `values[i]` is updated to be equal to `values[i - 1] + sum_value_digits`, `stdin` is empty, `i` is greater than or equal to `t` and has at least 1 digit, `sum_value_digits` is equal to the sum of all digits of `i`, `x` is the last digit of `i`.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: `t` is an integer greater than or equal to 0 and less than or equal to 10^4, `values` is a list of 2 * 10^5 + 1 integers where `values[i]` is the sum of all digits of `i` plus `values[i - 1]`, `stdin` is empty, `i` is greater than or equal to `t` and has at least 1 digit, `sum_value_digits` is equal to the sum of all digits of `i`, `x` is the last digit of `i`, `_` is `t`, `value` is an integer greater than or equal to `t` and has at least 1 digit, and the value of `values[value]` which is the sum of all digits of `value` plus `values[value - 1]` is being printed.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t integers. It calculates the cumulative sum of digits for all integers from 1 to 2 * 10^5, and then prints the cumulative sum of digits for each of the t input integers. The function does not return any value, but instead prints the results directly to the console.

