#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (1 <= n <= 2*10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9), where a_i is the initial number of stones in the i-th pile. The number of test cases is given in the first line of the input (1 <= t <= 10^4).
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
        
    #State: The loop has finished executing, and the output state is determined by the final values of the variables in the loop head and body. The variable _ has reached the value equal to the number of test cases in the input, stdin is empty, and the variables n, arr, s, ans, and i have the values determined by the last test case. If n is 2, 'Alice' is printed. If n is not 2, 'Alice' is printed if ans is 1, and 'Bob' is printed if ans is 0.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a number of piles and the initial number of stones in each pile. It then determines the winner of a game based on the number of piles and the differences in stone counts between consecutive piles. If there are only two piles, the function prints 'Alice'. If there are more than two piles, it checks the differences in stone counts between consecutive piles and prints 'Alice' if the last difference is greater than 1, otherwise it prints 'Bob'. The function processes all test cases and prints the winner for each case.

