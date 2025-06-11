#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 2*10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: tc is 0, n is an integer between 1 and 2*10^5, arr is a sorted list of unique integers in descending order with a 0 appended at the end, dp is True if arr[n-1] - arr[n] > 1 or not (arr[n-2] - arr[n-1] > 1 or not (... or not (arr[1] - arr[2] > 1))), stdin contains no test cases, i is n-1, and either 'Alice' or 'Bob' is printed depending on the value of dp.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of unique integers. It then determines whether the difference between consecutive integers in the sorted list is greater than 1 at any point, and prints 'Alice' if this condition is met, or 'Bob' otherwise. The function continues to process test cases until all input has been read.

