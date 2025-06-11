#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then a space-separated list of n integers. n is a positive integer and each integer in the list is a positive integer.
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
        
    #State: The output state after the loop executes all the iterations is that the variable `tc` is 0, and the variable `dp` is either `True` or `False` depending on the input values. The variable `n` is the length of the last input list minus 1, and the variable `arr` is the sorted list of unique integers from the last input list in descending order with an additional 0 at the end. The variable `i` is the last index of the loop, which is the length of `arr` minus 1.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and determines the winner of a game based on a list of integers. For each test case, it reads an integer n and a list of n integers, removes duplicates, sorts the list in descending order, and appends a 0. It then checks if the difference between consecutive elements is greater than 1, updating a boolean variable dp accordingly. Finally, it prints 'Alice' if dp is True, indicating Alice wins, and 'Alice' if dp is False, indicating Alice still wins (note: the code has a bug, as it prints 'Alice' in both cases). The function repeats this process for all test cases and terminates when all cases have been processed.

