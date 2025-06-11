#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The integer is a positive integer and represents the number of integers in the list. The list contains positive integers.
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
        
    #State: `tc` is 0, `n` is the number of unique integers in the input list, `arr` is a sorted list of unique integers from the list of the current test case in descending order with an additional element 0 at the end, `dp` is True if there exists at least one pair of adjacent elements in `arr` (excluding the last element 0) such that their difference is greater than 1, or False otherwise, `i` is equal to `n`, and either 'Alice' or 'Bob' is printed depending on the value of `dp`.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of a positive integer (n) followed by a list of positive integers. It removes duplicates from the list, sorts the unique integers in descending order, and appends a 0 to the end. Then, it checks if there exists at least one pair of adjacent elements (excluding the last element 0) with a difference greater than 1. Based on this condition, it prints either 'Alice' or 'Bob' for each test case. The function continues processing test cases until all input has been consumed.

