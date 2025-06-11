#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 500). Each test case contains three integers p_1, p_2 and p_3 (0 <= p_1 <= p_2 <= p_3 <= 30) — the scores of the three players, sorted non-decreasingly.
    t = int(input())
    for _ in range(t):
        p1, p2, p3 = map(int, input().split())
        
        if (p1 + p2 + p3) % 2 != 0:
            print(-1)
            continue
        
        if p3 >= p1 + p2:
            print(p1 + p2)
        else:
            x = 0
            y = p3
            while y >= x:
                if p1 - x <= p2 - y:
                    print(p1 - x + p3)
                    break
                else:
                    x += 1
                    y -= 1
            else:
                print(p3)
        
    #State: `t` is an integer between 0 and 500 inclusive, `_` is `t`, `p1`, `p2`, `p3` are integers between 0 and 30 inclusive, `p1` is less than or equal to `p2`, `p2` is less than or equal to `p3`. If the sum of `p1`, `p2`, and `p3` is even and `p3` is greater than or equal to `p1` + `p2`, the sum of `p1` and `p2` is printed. Otherwise, if the sum of `p1`, `p2`, and `p3` is even and `p3` is less than `p1` + `p2`, then `x` is equal to `y`.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. It then determines the maximum possible score that can be achieved by the first two players, considering the constraint that the sum of all three scores must be even. If the sum of the scores is odd, it prints -1. Otherwise, it prints the maximum possible score of the first two players, which is either the sum of their scores or the score of the third player, depending on the relative values of the scores.

