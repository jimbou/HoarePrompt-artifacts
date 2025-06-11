#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains a single integer n. The second line contains n integers a_1, a_2, ..., a_n. t, n, and a_i are positive integers. 1 <= t <= 10^4, 1 <= n <= 2*10^5, 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 2*10^5.
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
        
    #State: tc = 0

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and determines the winner ('Alice' or 'Bob') based on the provided integers. It takes no parameters and returns no value, but instead prints the winner for each test case. The function modifies the input integers by sorting and removing duplicates, and uses dynamic programming to evaluate the difference between consecutive integers. After processing all test cases, the function concludes with the variable 'tc' set to 0.

