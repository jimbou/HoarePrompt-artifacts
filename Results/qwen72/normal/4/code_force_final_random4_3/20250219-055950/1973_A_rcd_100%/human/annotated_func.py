#State of the program right berfore the function call: The function should take three integers p_1, p_2, and p_3 as input, where 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30, and these integers represent the scores of three players after playing chess games. The function should also handle multiple test cases, where the number of test cases t is an integer such that 1 ≤ t ≤ 500.
def func():
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
        
    #State: After all iterations, `p1`, `p2`, and `p3` are integers provided by user input, with `p1` ≤ `p2` ≤ `p3` ≤ 30, and the sum of `p1`, `p2`, and `p3` is odd. `t` is the total number of test cases, and `_` is `t - 1`. If `p3` is greater than or equal to `p1 + p2`, the program continues to the next iteration of the loop. Otherwise, if `p1 - x` ≤ `p2 - y` at any point, the loop breaks and prints `p1 - x + p3`. If this condition is never met, the loop continues until `y < x`, and then prints `p3`. The values of `x` and `y` will be such that `x` is the number of iterations the loop has run, and `y` is `p3 - x`. The other variables (`p1`, `p2`, `p3`, `t`) remain unchanged.
#Overall this is what the function does:The function `func` accepts an integer `t` representing the number of test cases and, for each test case, three integers `p1`, `p2`, and `p3` representing the scores of three players, with the constraints 1 ≤ t ≤ 500 and 0 ≤ p1 ≤ p2 ≤ p3 ≤ 30. For each test case, it performs the following actions: If the sum of the scores is odd, it prints -1. If the score of the third player (`p3`) is greater than or equal to the sum of the scores of the first two players (`p1 + p2`), it prints `p1 + p2`. Otherwise, it iterates through a loop to find a point where `p1 - x` is less than or equal to `p2 - y` and prints `p1 - x + p3`. If no such point is found, it prints `p3`. The function does not return any values, but it prints the result for each test case.

