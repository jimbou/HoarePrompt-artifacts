#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers p_1, p_2 and p_3 (0 <= p_1 <= p_2 <= p_3 <= 30) — the scores of the three players, sorted non-decreasingly.
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
        
    #State: The output state will be a list of integers, each representing the maximum number of points that can be scored by the three players in each test case, or -1 if it is not possible to score any points. The list will have the same number of elements as the number of test cases, and each element will be the result of the calculations performed inside the loop for the corresponding test case.

#Overall this is what the function does:Calculates the maximum number of points that can be scored by three players in a game, given their scores, and outputs the results for multiple test cases. The function takes no arguments, reads input from stdin, and prints the results. For each test case, it either outputs -1 if the total score is odd or the maximum achievable score based on the players' scores, following specific rules to determine the optimal score. The output is a list of integers, each representing the maximum score for a test case, with the same number of elements as the number of test cases.

