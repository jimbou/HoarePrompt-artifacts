#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains a single integer n. The second line contains n integers a_1, a_2, … a_n. t, n and a_i are positive integers such that 1 <= t <= 10^4 and 1 <= n <= 2*10^5 and 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 2*10^5.
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
        
    #State: tc is 0, n is a positive integer between 1 and 2*10^5, arr is a list of distinct positive integers in descending order with a 0 appended at the end, dp is True if arr[i] - arr[i+1] > 1 for any i in range(1, len(arr)-1) or False otherwise, stdin is empty, i is 0, and 'Alice' is printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints 'Alice' for each case. It accepts a series of test cases, where each case consists of a positive integer n and a list of distinct positive integers in descending order. The function checks if the difference between any two consecutive integers in the list is greater than 1 and prints 'Alice' accordingly. After processing all test cases, the function leaves the input stream empty.

