#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t space-separated integers x (2 <= x <= 1000).
    num = int(input('Enter number of entries- '))
    L1 = []
    res = []
    for i in range(num):
        L1.append(int(input('Enter entry no.' + str(i + 1) + '- ')))
        
    #State: Output State: num is t, L1 is a list containing t integers x, res is an empty list, stdin is empty.
    for i in range(num):
        for j in range(2, L1[i] + 1):
            if L1[i] % j == 0:
                res.append(L1[i] // j * (j - 1))
                break
        
    #State: Output State: num is t, L1 is a list containing t integers x, res is a list containing at most t integers, stdin is empty.
    #
    #In natural language, the output state is: The number of iterations is still t, the list L1 remains unchanged with t integers, the result list res now contains at most t integers (one for each iteration of the outer loop), and the standard input stdin is still empty.
    print(*res, sep='\n')
    #This is printed: at most t integers, one for each iteration of the outer loop, separated by newline characters

#Overall this is what the function does:The function takes an integer t and t space-separated integers x as input from the user, and for each integer x, it calculates and prints the product of the integer divided by its smallest divisor greater than 1 and the divisor minus 1, if such a divisor exists. If no such divisor exists for an integer x, it does not print anything for that integer. The function prints at most t integers, one for each input integer x, separated by newline characters.

