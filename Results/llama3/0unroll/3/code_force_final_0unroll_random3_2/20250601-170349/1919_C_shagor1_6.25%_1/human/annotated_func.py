#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 ≤ n ≤ 2*10^5) and then a list of n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ n).
    for _ in range(int(input())):
        n = int(input())
        
        *inp, = map(int, input().split())
        
        x = y = n + 1
        
        ans = 0
        
        for a in inp:
            if a <= x:
                x = a
            elif a <= y:
                y = a
            else:
                x == y
                y = a
                ans += 1
        
        print(ans)
        
    #State: The number of times the value of y was updated when the current value of a is greater than both x and y, for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then processes the list to find the number of times the largest value (y) needs to be updated when the current value is greater than both the largest (y) and second largest (x) values. The function prints the count of such updates for each test case.

