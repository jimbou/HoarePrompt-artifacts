#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a, b <= 10^9.
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns the string 'Bob'
    else :
        return 'Alice'
        #The program returns the string 'Alice'.

#Overall this is what the function does:Determines the winner of a game based on the sum of two non-negative integers, returning 'Bob' if the sum is even and 'Alice' if the sum is odd.

#State of the program right berfore the function call: t is a positive integer, a and b are positive integers.
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: Output State: t is an integer equal to the user's input, a and b are the last pair of positive integers input by the user, results is a list of the winners of each iteration, stdin is empty.
    for result in results:
        print(result)
        
    #State: Output State: t is an integer equal to the user's input, a and b are the last pair of positive integers input by the user, results is an empty list, stdin is empty.

#Overall this is what the function does:Determines the winner of a game or competition between two players, given their respective scores or values, and returns the winner.

