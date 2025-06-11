#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). Each test case contains three integers p_1, p_2 and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) — the scores of the three players, sorted non-decreasingly.
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: `t` is an integer equal to 0, `v` is a list of three integers `p_1`, `p_2` and `p_3` (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30), stdin contains multiple test cases - 1. If the sum of `p_1`, `p_2`, and `p_3` is odd, -1 is printed. Otherwise, the average of `p_1`, `p_2`, and `p_3` is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. It then calculates and prints the average score of the three players, but only if the sum of their scores is even. If the sum is odd, it prints -1. The function processes all test cases and does not return any value.

