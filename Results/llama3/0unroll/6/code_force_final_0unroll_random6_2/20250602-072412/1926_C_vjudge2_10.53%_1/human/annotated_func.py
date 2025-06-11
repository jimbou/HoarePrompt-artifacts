#State of the program right berfore the function call: stdin contains two inputs: first an integer (greater than 0 and less or equal than 10^4) and then a sequence of integers (each greater than 0 and less or equal than 2*10^5).
    t = int(input())
    numbers = []
    for _ in range(t):
        n = int(input())
        
        numbers.append(n)
        
    #State: Output State: t is an integer greater than or equal to 0 and less or equal than 10^4, numbers is a list of integers (each greater than 0 and less or equal than 2*10^5) of length t, stdin is empty.
    values = [(0) for _ in range(max(numbers) + 1)]
    sum_values = [(0) for _ in range(max(numbers) + 1)]
    total = 0
    for i in range(10):
        values[i] = i
        
        total += i
        
        sum_values[i] = total
        
    #State: Output State: t is an integer greater than or equal to 0 and less or equal than 10^4, numbers is a list of integers (each greater than 0 and less or equal than 2*10^5) of length t, values is a list of integers of length max(numbers) + 1 where the first 10 elements are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 and the rest are unchanged, sum_values is a list of integers of length max(numbers) + 1 where the first 10 elements are 0, 1, 3, 6, 10, 15, 21, 28, 36, 45 and the rest are unchanged, total is 45.
    for i in range(10, n + 1):
        word = str(i)
        
        last = int(word[len(word) - 1])
        
        remainder = int(word[:-1])
        
        values[i] = values[last] + values[remainder]
        
        sum_total = values[i] + sum_values[i - 1]
        
        sum_values[i] = sum_total
        
    #State: Output State: t is an integer greater than or equal to 0 and less or equal than 10^4, numbers is a list of integers (each greater than 0 and less or equal than 2*10^5) of length t, values is a list of integers of length max(numbers) + 1 where the first 10 elements are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 and the rest are calculated based on the last digit and the remaining digits of the number, sum_values is a list of integers of length max(numbers) + 1 where the first 10 elements are 0, 1, 3, 6, 10, 15, 21, 28, 36, 45 and the rest are calculated based on the values and sum_values of the previous number, total is 45.
    for n in numbers:
        print(sum_values[n])
        
    #State: Output State: The loop iterates over the list of numbers and prints the sum of values for each number. The sum_values list is updated based on the values and sum_values of the previous number. The total variable remains unchanged at 45. The output state is the same as the initial state, with the addition of the printed sum of values for each number in the numbers list.

#Overall this is what the function does:This function reads a sequence of integers from standard input, calculates a custom sum of values for each number based on its digits, and prints the calculated sums. The function first initializes two lists, values and sum_values, to store the custom sum of values for each number from 0 to the maximum number in the input sequence. It then calculates the custom sum of values for each number in the input sequence by considering the last digit and the remaining digits of the number. Finally, it prints the calculated sum of values for each number in the input sequence.

