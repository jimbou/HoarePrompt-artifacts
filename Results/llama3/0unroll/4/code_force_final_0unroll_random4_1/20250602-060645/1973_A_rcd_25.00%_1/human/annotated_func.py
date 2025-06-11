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
        
    #State: The output state will be a list of integers, each representing the maximum number of points that can be scored by the three players in each test case, or -1 if it is not possible to score an even number of points. The list will have a length of t, where t is the number of test cases. The value of t will remain unchanged, as it is not affected by the loop.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. It then calculates and prints the maximum number of points that can be scored by the players in each test case, or -1 if it's not possible to score an even number of points. The function processes all test cases and outputs a list of integers, each representing the maximum score for the corresponding test case.

