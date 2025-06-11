#State of the program right berfore the function call: stdin contains two inputs: first an integer (between 1 and 10^4 inclusive) and then a sequence of integers (between 1 and 2*10^5 inclusive), each on a new line.
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: Output State: The value of the variable "values" has been updated such that each index "i" contains the sum of the digits of all integers from 1 to "i". The rest of the variables remain unchanged.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: Output State: The value of the variable "t" has been decremented by the number of iterations of the loop, and the value of the variable "values" has been updated such that each index "i" contains the sum of the digits of all integers from 1 to "i" plus the sum of the digits of the input values. The rest of the variables remain unchanged.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t integers. It then calculates the sum of the digits of all integers from 1 to each input integer and prints the result. The function does not modify the input values or any other variables, and its output is solely based on the input values.

