#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a, b <= 10^9.
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns the string 'Bob'.
    else :
        return 'Alice'
        #The program returns the string 'Alice'

#Overall this is what the function does:Determines the winner ('Bob' or 'Alice') based on whether the sum of two non-negative integers (a and b) is even or odd.

#State of the program right berfore the function call: t is a positive integer, a and b are positive integers.
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: t is 0, a is a positive integer equal to the last input, b is a positive integer equal to the last input, results is a list containing the results of func_1(a, b) for all inputs, stdin is empty, _ is t
    for result in results:
        print(result)
        
    #State: t is 0, a is a positive integer equal to the last input, b is a positive integer equal to the last input, results is an empty list, stdin is empty, _ is t, and all results of func_1(a, b) have been printed

#Overall this is what the function does:Determines the winner of a game for multiple test cases and prints the results. The function accepts two positive integers, a and b, and returns the winner of the game. The function is called repeatedly for a specified number of test cases, and the results are stored in a list. After all test cases have been processed, the results are printed to the console. The function does not modify the input variables a and b, and the final state of the program is that all results have been printed and the input buffer is empty.

