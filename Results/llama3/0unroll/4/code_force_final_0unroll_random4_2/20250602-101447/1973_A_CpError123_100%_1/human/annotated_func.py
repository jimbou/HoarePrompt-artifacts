#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers p_1, p_2 and p_3 (0 <= p_1 <= p_2 <= p_3 <= 30) — the scores of the three players, sorted non-decreasingly.
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        if (a + b + c) % 2 != 0:
            print(-1)
            continue
        
        x = (a + b + c) // 2
        
        y = a + b
        
        print(min(x, y))
        
    #State: The output state will contain the minimum of the sum of the first two scores and half of the total sum of the three scores for each test case, or -1 if the total sum of the three scores is odd. The number of test cases will be one less than the initial value of `t`.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. It calculates and prints the minimum of the sum of the first two scores and half of the total sum of the three scores for each test case. If the total sum of the three scores is odd, it prints -1 instead. The function processes all test cases and outputs the results accordingly.

