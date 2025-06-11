#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2*10^5) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases is between 1 and 10^4.
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        s = set()
        
        for i in range(n):
            s.add(arr[i])
        
        s = list(s)
        
        ans = 1
        
        s = [0] + s
        
        n = len(s)
        
        if n == 2:
            print('Alice')
        else:
            for i in range(1, n - 1):
                if s[i] - s[i - 1] > 1:
                    break
                else:
                    ans = 1 - ans
            if ans:
                print('Alice')
            else:
                print('Bob')
        
    #State: stdin is empty, _ is the number of test cases, n is 0, arr is an empty list, s is an empty list, ans is 0.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains an integer n and a list of n integers. It determines the winner of a game based on the list of integers, printing 'Alice' or 'Bob' for each test case. The function iterates through all test cases, leaving the standard input empty and variables in a reset state after execution.

