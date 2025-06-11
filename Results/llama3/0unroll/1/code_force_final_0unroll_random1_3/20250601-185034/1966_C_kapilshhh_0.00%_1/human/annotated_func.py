#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2*10^5) and then n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases is a positive integer (1 <= t <= 10^4).
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
        
    #State: tc = 0, n = 0, arr = [], dp = True

#Overall this is what the function does:This function determines the winner of a game based on a given set of integers. It reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. The function sorts the integers in descending order, removes duplicates, and checks if the difference between consecutive integers is greater than 1. If such a difference is found, the function prints 'Alice', indicating that Alice wins the game. Otherwise, it prints 'Alice' as well, indicating that Alice still wins. The function processes all test cases and does not return any value.

