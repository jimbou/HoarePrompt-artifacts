#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). Each test case contains three integers p_1, p_2 and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) — the scores of the three players, sorted non-decreasingly.
    t = int(input())
    for _ in range(t):
        p1, p2, p3 = map(int, input().split())
        
        if (p1 + p2 + p3) % 2 != 0:
            print(-1)
            continue
        
        if p3 >= p1 + p2:
            print(p1 + p2)
        else:
            low, high = min(p3 - p1, p3 - p2), max(p3 - p1, p3 - p2)
            cur = low
            while high >= cur:
                if p1 - cur <= p2 - (p3 - cur):
                    print(p1 - cur + p3)
                    break
                else:
                    cur += 1
            else:
                print(p3)
        
    #State: `t` is 0, `_` is `t`, `p1`, `p2`, and `p3` are integers assigned values from the input, stdin contains multiple test cases (with the first line consumed).

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. It then determines the maximum possible score that can be achieved by redistributing the scores among the players, subject to certain constraints, and prints the result for each test case. If the total score is odd or if the highest score is greater than or equal to the sum of the other two scores, it prints -1 or the sum of the two lower scores, respectively. Otherwise, it iteratively adjusts the scores to find the maximum possible score that can be achieved while satisfying the constraints.

