#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers p_1, p_2 and p_3 (0 <= p_1 <= p_2 <= p_3 <= 30) — the scores of the three players, sorted non-decreasingly.
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: The output state will contain the results of the calculations for each test case, either '-1' if the sum of the three integers is odd, or the calculated result if the sum is even. The value of 't' remains unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. It calculates and prints the result for each test case, which is either '-1' if the sum of the scores is odd, or a calculated value if the sum is even. The function does not modify the input values or any external state, and its output is solely based on the input test cases.

