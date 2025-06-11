#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains six integers h, w, x_a, y_a, x_b, y_b such that 1 <= x_a, x_b <= h <= 10^6 and 1 <= y_a, y_b <= w <= 10^9. The first line contains a single integer t (1 <= t <= 10^4) — the number of test cases.
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
        
    #State: The output state after the loop executes all the iterations is a list of strings, where each string is either 'Draw', 'Alice', or 'Bob', indicating the winner of each test case. The list has the same length as the number of test cases (t) in the initial state.

#Overall this is what the function does:Determines the winner of a game for each test case, where two players 'Alice' and 'Bob' start at positions (xa, ya) and (xb, yb) respectively on a grid of size h x w, and prints the result as either 'Draw', 'Alice', or 'Bob' for each test case.

