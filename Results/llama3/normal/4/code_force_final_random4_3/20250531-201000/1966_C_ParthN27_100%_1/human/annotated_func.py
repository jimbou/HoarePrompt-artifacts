#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 2*10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        s = set()
        
        for i in range(n):
            s.add(arr[i])
        
        s = list(s)
        
        s.sort()
        
        s = [0] + s
        
        ans = 1
        
        n = len(s)
        
        if n == 2:
            print('Alice')
        else:
            for i in range(1, n - 1):
                if s[i] - s[i - 1] > 1:
                    break
                else:
                    ans ^= 1
            if ans:
                print('Alice')
            else:
                print('Bob')
        
    #State: stdin is empty, _ is t, arr is a list of integers, s is a sorted list of integers with 0 prepended, ans is either 0 or 1, i is an integer greater than or equal to 0, n is the number of elements in s.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then determines the winner of a game based on the given integers, either 'Alice' or 'Bob', and prints the result. The function processes all test cases and leaves the standard input empty after execution.

