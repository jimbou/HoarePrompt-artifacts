#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers p_1, p_2 and p_3 (0 <= p_1 <= p_2 <= p_3 <= 30) — the scores of the three players, sorted non-decreasingly.
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: The output state is a list of integers, where each integer is the result of the calculation (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2 for each test case, or -1 if the sum of the three integers in the test case is odd. The value of `t` is unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. It calculates the result for each test case by subtracting the maximum of 0 and the difference between the highest and the sum of the two lowest scores from the total score, then dividing by 2. If the total score is odd, it outputs -1. The function outputs a list of results, one for each test case, without modifying the input value `t`.

