#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains six integers h, w, x_a, y_a, x_b, y_b such that 1 <= x_a, x_b <= h <= 10^6 and 1 <= y_a, y_b <= w <= 10^9.
    t = int(input())
    for _ in range(t):
        r, w, a, b, c, d = list(map(int, input().split()))
        
        if a > c:
            print('Draw')
        else:
            x = abs(a - c) // 2
            if abs(a - c) % 2:
                l = max(1, d - x)
                r = min(w, d + x)
                print(*(['Draw'], ['Alice'])[abs(l - b) <= x + 1 and abs(r - b) <= 
                    x + 1])
            else:
                l = max(1, b - x)
                r = min(w, b + x)
                print(*(['Draw'], ['Bob'])[abs(l - d) <= x and abs(r - d) <= x])
        
    #State: `t` is 0, `r`, `w`, `a`, `b`, `c`, and `d` are integers, `_` is `t`, stdin contains no test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing six integers representing the dimensions of a rectangle and the positions of two points, Alice and Bob. It then determines the winner of a game based on the relative positions of Alice and Bob, printing 'Draw' if the game is a draw, 'Alice' if Alice wins, or 'Bob' if Bob wins. The function processes all test cases and prints the results for each case.

