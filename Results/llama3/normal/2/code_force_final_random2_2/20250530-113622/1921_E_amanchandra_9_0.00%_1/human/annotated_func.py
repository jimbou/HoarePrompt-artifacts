#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains six integers h, w, x_a, y_a, x_b, y_b such that 1 <= x_a, x_b <= h <= 10^6 and 1 <= y_a, y_b <= w <= 10^9. The first integer t (1 <= t <= 10^4) represents the number of test cases.
    for i in range(int(input())):
        h, w, xa, ya, xb, yb = map(int, input().split())
        
        if xa > xb:
            print('Draw')
        else:
            x = abs(xa - xb) // 2
            if abs(xa - xb) % 2:
                l = max(1, yb - x)
                r = min(w, yb + x)
                print(*(['Draw'], ['Alice'])[abs(l - ya) <= x + 1 and abs(r - ya) <=
                    x + 1])
            else:
                l = max(1, ya - x)
                r = min(w, yb + x)
                print(*(['Draw'], ['Bob'])[abs(l - yb) <= x and abs(r - yb) <= x])
        
    #State: All test cases have been processed, and the output for each test case has been printed. The loop has executed `t` times, where `t` is the number of test cases. The variables `h`, `w`, `xa`, `ya`, `xb`, and `yb` have been assigned values from the input for each test case. The output for each test case is either 'Draw', 'Alice', or 'Bob', depending on the conditions specified in the loop body.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains six integers representing the dimensions of a rectangle and the positions of two points. It determines the winner of a game based on the positions of the points and the dimensions of the rectangle, printing 'Draw' if there is no winner, 'Alice' if Alice wins, or 'Bob' if Bob wins. The function iterates over all test cases, processing each one independently and printing the result for each case.

