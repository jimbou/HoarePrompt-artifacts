#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a, b <= 10^9.
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns the string 'Bob'.
    else :
        return 'Alice'
        #The program returns the string 'Alice'

#Overall this is what the function does:Determines the winner of a game based on the sum of two non-negative integers, returning 'Bob' if the sum is even and 'Alice' if the sum is odd.

#State of the program right berfore the function call: t is a positive integer, a and b are positive integers
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: t is an integer equal to 0, a and b are positive integers, results is a list containing the return values of func_1(a, b) for each iteration of the loop, stdin is empty.
    for result in results:
        print(result)
        
    #State: t is 0, a and b are positive integers, results is a list containing the return values of func_1(a, b) for each iteration of the loop, stdin is empty, and all results in the list have been printed.

#Overall this is what the function does:The function accepts a positive integer t, and for each iteration of t, it accepts two positive integers a and b, processes them, and returns a result. The function repeats this process t times, storing each result in a list. After processing all iterations, the function prints each result in the list. The final state of the program is that all results have been printed, and the input buffer (stdin) is empty.

