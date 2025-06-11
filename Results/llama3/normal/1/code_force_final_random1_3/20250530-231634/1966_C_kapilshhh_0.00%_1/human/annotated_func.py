#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then a list of n integers. n is a positive integer and each integer in the list is a positive integer.
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
        
    #State: tc is 0, stdin contains no test cases, arr is a list of unique positive integers in descending order with an extra 0 at the end, dp is True if the difference between any two consecutive elements in arr is greater than 1, otherwise it's False, i is n, and 'Alice' is printed t times.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a positive integer n followed by a list of n positive integers. It then processes each test case by removing duplicates from the list, sorting the remaining integers in descending order, and appending a 0 to the end. The function checks if the difference between any two consecutive elements in the sorted list is greater than 1 and prints 'Alice' if this condition is met, otherwise it prints 'Alice' as well. The function repeats this process for all test cases and does not return any value.

