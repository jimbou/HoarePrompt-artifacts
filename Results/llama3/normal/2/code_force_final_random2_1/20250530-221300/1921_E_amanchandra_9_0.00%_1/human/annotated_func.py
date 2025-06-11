#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 10^4) — the number of test cases. Each test case consists of a single line containing six integers h, w, x_a, y_a, x_b, y_b (1 <= x_a, x_b <= h <= 10^6, 1 <= y_a, y_b <= w <= 10^9) — the dimensions of the board and the initial positions of Alice's and Bob's chips. It is guaranteed that either x_a != x_b or y_a != y_b.
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
        
    #State: h, w, xa, ya, xb, yb are integers, i is equal to the number of test cases, stdin contains no test cases. If xa > xb, 'Draw' is printed. Otherwise, x is the integer part of the absolute difference between xa and xb divided by 2. If abs(xa - xb) is odd, either 'Draw' or 'Alice' is printed based on the conditions abs(l - ya) <= x + 1 and abs(r - ya) <= x + 1, where l is the maximum of 1 and yb - x, and r is the minimum of w and yb + x. If abs(xa - xb) is even, either 'Draw' or 'Bob' is printed based on the conditions abs(l - yb) <= x and abs(r - yb) <= x, where l is the maximum of 1 and ya - x, and r is the minimum of w and yb + x.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of six integers representing the dimensions of a board and the initial positions of Alice's and Bob's chips. It then determines the winner of a game based on the positions of the chips and prints either 'Draw', 'Alice', or 'Bob' to the console. The function processes all test cases and prints the result for each case, leaving the standard input empty after execution.

