#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then n space-separated integers. t is a positive integer, n is a positive integer, and the integers are positive and do not exceed 10^9.
    tc = int(input())
    while tc > 0:
        n = int(input())
        
        arr = sorted(list(set([int(x) for x in input().split(' ')])), reverse=True) + [
            0]
        
        dp = True
        
        n = len(arr) - 1
        
        for i in range(1, n):
            dp = arr[i] - arr[i + 1] > 1 or not dp
        
        print('Alice' if dp else 'Bob')
        
        tc -= 1
        
    #State: The output state will be a series of strings, either 'Alice' or 'Bob', one for each test case.

#Overall this is what the function does:Determines the winner of a game for each test case by analyzing a sorted list of unique integers. The function takes no arguments and returns a series of strings, either 'Alice' or 'Bob', indicating the winner of each test case. The output is based on the difference between consecutive integers in the sorted list, with 'Alice' winning if the difference is greater than 1 at any point, and 'Bob' winning otherwise.

