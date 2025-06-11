#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers p_1, p_2 and p_3 (0 <= p_1 <= p_2 <= p_3 <= 30) — the scores of the three players, sorted non-decreasingly.
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: `_` is equal to `t`, `v` is a list of three integers from the input, stdin contains no test cases. If the sum of the elements of `v` is odd, -1 is printed. Otherwise, if the third element of `v` is less than or equal to the sum of the first two elements, the average of the first two elements of `v` plus half of the third element of `v` is printed. Otherwise, the average of the first two elements of `v` is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. It then calculates and prints the maximum possible score that can be achieved by combining the scores of the players, considering the constraint that the sum of the scores must be even. If the sum of the scores is odd, it prints -1. Otherwise, it prints the average of the first two scores plus half of the third score if the third score is less than or equal to the sum of the first two scores; otherwise, it prints the average of the first two scores.

