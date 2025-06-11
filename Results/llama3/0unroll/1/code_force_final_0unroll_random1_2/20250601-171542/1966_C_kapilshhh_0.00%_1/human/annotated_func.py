#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then a space-separated list of n integers. t is a positive integer, n is a positive integer, and the integers in the list are positive integers.
    tc = int(input())
    while tc > 0:
        n = int(input())
        
        arr = sorted(list(set([int(x) for x in input().split(' ')])), reverse=True) + [
            0]
        
        dp = True
        
        n = len(arr) - 1
        
        for i in range(1, len(arr)):
            dp = arr[i] - (arr[i + 1] if i < n else 0) > 1 or not dp
        
        print('Alice' if dp else 'Alice')
        
        tc -= 1
        
    #State: The output state is a list of strings, where each string is either 'Alice' or 'Bob', depending on the value of dp after each iteration of the loop.

#Overall this is what the function does:Determines the winner of a game for each test case by processing a list of integers, and prints the result as either 'Alice' or 'Bob'. The function takes no arguments and returns no value, instead printing the outcome of each test case.

