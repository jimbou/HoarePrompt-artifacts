#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers p_1, p_2 and p_3 (0 <= p_1 <= p_2 <= p_3 <= 30) — the scores of the three players, sorted non-decreasingly.
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: `t` is 0, `_` is `t`, `v` is a list of three integers p_1, p_2, and p_3 (0 <= p_1 <= p_2 <= p_3 <= 30) from the input, stdin is empty. If the sum of the elements in `v` is odd, -1 is printed. Otherwise, the result is calculated as (p_1 + p_2 + p_3 - max(0, p_3 - p_1 - p_2)) // 2 and printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. It then calculates and prints the maximum possible score that can be achieved by the players, or -1 if the total score is odd. The function processes all test cases and empties the standard input.

