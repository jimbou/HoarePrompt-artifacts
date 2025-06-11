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
        
    #State: `t` is 0, `_` is `t`, `p1`, `p2`, `p3` are integers, stdin is empty. If the sum of `p1`, `p2`, and `p3` is odd, -1 is printed. Otherwise, `p1`, `p2` are integers, `p3` is greater than or equal to 0, `y` is greater than or equal to 0, and `x` is either 0 or a positive integer. If `p3` is greater than or equal to `p1` + `p2`, the sum of `p1` and `p2` is printed. If `p3` is less than `p1` + `p2`, then if `p1` - `x` is less than or equal to `p2` - `y`, the program breaks out of the most internal loop or if statement with `x` being 0, 1, 2, or 3, and `y` being greater than or equal to 0. Otherwise, `x` is 1, 2, or 3, and `y` is greater than or equal to 1.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. It then determines the maximum possible score that can be achieved by the first two players, either by summing their scores or by finding a combination of scores that satisfies certain conditions. If the sum of the three scores is odd, it prints -1. Otherwise, it prints the maximum possible score that can be achieved by the first two players. The function processes all test cases and prints the results accordingly.

