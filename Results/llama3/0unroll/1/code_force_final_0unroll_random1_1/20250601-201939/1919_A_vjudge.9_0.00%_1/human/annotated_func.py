#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a, b <= 10^9.
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns the string 'Bob'
    else :
        return 'Alice'
        #The program returns the string 'Alice'.

#Overall this is what the function does:Determines the winner ('Bob' or 'Alice') based on whether the sum of two non-negative integers (a and b) is even or odd.

#State of the program right berfore the function call: t is a positive integer, a and b are positive integers.
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: Output State: t is a positive integer equal to the user's input, a and b are the last pair of positive integers input by the user, results is a list of t elements where each element is the output of func_1 for the corresponding pair of input integers a and b.
    for result in results:
        print(result)
        
    #State: Output State: t is a positive integer equal to the user's input, a and b are the last pair of positive integers input by the user, results is a list of t elements where each element is the output of func_1 for the corresponding pair of input integers a and b.

#Overall this is what the function does:Determines the winner for each pair of input integers and returns the result.

