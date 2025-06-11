#State of the program right berfore the function call: stdin contains two inputs: first an integer (greater than 0 and less than or equal to 10^4) and then a list of integers (each greater than 0 and less than or equal to 2 * 10^5).
    t = int(input())
    numbers = []
    for _ in range(t):
        n = int(input())
        
        numbers.append(n)
        
    #State: Output State: t is 0, numbers is a list of t integers.
    values = [(0) for _ in range(max(numbers) + 1)]
    sum_values = [(0) for _ in range(max(numbers) + 1)]
    total = 0
    for i in range(10):
        values[i] = i
        
        total += i
        
        sum_values[i] = total
        
    #State: Output State: t is 0, numbers is a list of t integers, values is a list of 10 integers where the value at index i is i, sum_values is a list of 10 integers where the value at index i is the sum of all integers from 0 to i, total is 45.
    for i in range(10, n + 1):
        word = str(i)
        
        last = int(word[len(word) - 1])
        
        remainder = int(word[:-1])
        
        values[i] = values[last] + values[remainder]
        
        sum_total = values[i] + sum_values[i - 1]
        
        sum_values[i] = sum_total
        
    #State: Output State: t is 0, numbers is a list of t integers, values is a list of 11 integers where the value at index i is the sum of all integers from 0 to i, sum_values is a list of 11 integers where the value at index i is the sum of all integers from 0 to i, total is 55.
    for n in numbers:
        print(sum_values[n])
        
    #State: Output State: t is 0, numbers is a list of t integers, values is a list of 11 integers where the value at index i is the sum of all integers from 0 to i, sum_values is a list of 11 integers where the value at index i is the sum of all integers from 0 to i, total is 55.

#Overall this is what the function does:This function reads a series of integers from standard input, calculates the sum of digits for each integer, and prints the cumulative sum of these sums for each integer. The function takes no explicit parameters and returns no value, instead printing the results directly to the console. The input integers are expected to be greater than 0 and less than or equal to 2 * 10^5. The function initializes two lists, values and sum_values, to store the sum of digits and cumulative sum of these sums, respectively. It then iterates over the input integers, calculates the sum of digits for each integer, and updates the values and sum_values lists accordingly. Finally, it prints the cumulative sum of sums for each integer.

