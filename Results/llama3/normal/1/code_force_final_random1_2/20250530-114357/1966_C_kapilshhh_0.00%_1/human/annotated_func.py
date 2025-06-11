#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The integer is a positive integer and represents the number of integers in the list. The list contains positive integers.
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
        
    #State: tc is 0, n is the number of unique positive integers in the list minus 1, arr is a sorted list of unique positive integers from the list in descending order with a 0 appended at the end and its length is at least 2, dp is True if there exists a pair of adjacent elements in the list (or the last element and 0) with a difference greater than 1, otherwise False, stdin contains no test cases, i is n, and 'Alice' is printed for every test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n followed by a list of n positive integers. It then processes each test case by removing duplicates from the list, sorting the remaining integers in descending order, and appending a 0 to the end of the list. The function checks if there exists a pair of adjacent elements in the list (or the last element and 0) with a difference greater than 1, and prints 'Alice' if such a pair is found, otherwise it prints 'Alice' as well. The function repeats this process for all test cases until standard input is exhausted.

