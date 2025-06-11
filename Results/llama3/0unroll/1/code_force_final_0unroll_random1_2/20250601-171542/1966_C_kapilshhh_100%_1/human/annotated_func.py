#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2*10^5) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: tc is 0, and the values of the variables n, arr, and dp have been updated according to the last test case.

#Overall this is what the function does:This function determines the winner of a game based on a list of integers. It takes a list of integers as input, removes duplicates, sorts them in descending order, and then checks if the difference between consecutive integers is greater than 1. If this condition is met, it prints 'Alice', otherwise it prints 'Bob'. The function processes multiple test cases, each containing a list of integers, and prints the winner for each case.

