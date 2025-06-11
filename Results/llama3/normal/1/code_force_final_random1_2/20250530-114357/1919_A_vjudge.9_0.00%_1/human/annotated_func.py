#State of the program right berfore the function call: a and b are positive integers representing the number of coins in Alice's and Bob's wallets, respectively.
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns the string 'Bob'
    else :
        return 'Alice'
        #The program returns the string 'Alice'.

#Overall this is what the function does:Determines the winner based on the total number of coins in Alice's and Bob's wallets. If the total is even, the function returns 'Bob', indicating Bob as the winner. If the total is odd, the function returns 'Alice', indicating Alice as the winner.

#State of the program right berfore the function call: t is a positive integer, a and b are positive integers
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: t is an integer equal to 0, a is a positive integer equal to the first integer from the input, b is a positive integer equal to the second integer from the input, results is a list containing the result of func_1(a, b) repeated t times, stdin is empty, _ is t-1
    for result in results:
        print(result)
        
    #State: `t` is 0, `a` is a positive integer equal to the first integer from the input, `b` is a positive integer equal to the second integer from the input, `results` is a list containing the result of func_1(a, b) repeated t times, `stdin` is empty, `_` is -1, and all elements in the `results` list have been printed.

#Overall this is what the function does:The function reads a specified number of test cases from standard input, where each test case consists of two positive integers. It then calls another function, func_1, with these integers as arguments, and appends the result to a list. After processing all test cases, it prints each result in the list. The function does not modify the input values or perform any other actions beyond reading input, calling func_1, and printing results.

