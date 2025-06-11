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
        
    #State: `t` is 0, `_` is `t`, `p1`, `p2`, `p3` are integers between 0 and 30, `p1` is less than or equal to `p2`, `p2` is less than or equal to `p3`, stdin contains no input. If the sum of `p1`, `p2`, and `p3` is odd, then -1 is printed. If `p3` is greater than or equal to `p1` + `p2`, the sum of `p1` and `p2` is printed. Otherwise, `p3` must be greater than 1, and `x` is equal to `y`, which is equal to `p3 - 1` or `p3 - 2` or `p3 - 3` or ... or `0`.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. It then determines and prints the maximum possible score that can be achieved by rearranging the scores, considering the constraints that the sum of the scores must be even and the scores must be non-decreasing. If the sum of the scores is odd, it prints -1. If the highest score is greater than or equal to the sum of the other two scores, it prints the sum of the two lower scores. Otherwise, it calculates and prints the maximum possible score by iteratively adjusting the scores.

