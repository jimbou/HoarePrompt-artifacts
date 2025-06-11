#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2*10^5) and then n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases is a positive integer (1 <= t <= 10^4).
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
        
    #State: `tc` is 0, `n` is a positive integer (1 <= n <= 2*10^5 + 1), `arr` is a sorted list of distinct integers in descending order with a 0 appended at the end, `i` is 1, `dp` is True if there is at least one pair of adjacent elements in `arr` with a difference greater than 1, False otherwise, and either 'Alice' or 'Bob' is printed depending on the value of `dp`. If `dp` is True, 'Alice' is printed, otherwise 'Bob' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n distinct integers. It then determines whether there exists at least one pair of adjacent integers with a difference greater than 1. If such a pair exists, it prints 'Alice'; otherwise, it prints 'Bob'. The function processes all test cases and prints the corresponding results.

