#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains six integers: h, w, x_a, y_a, x_b, y_b. h and w are positive integers representing the dimensions of the board. x_a, y_a, x_b, and y_b are positive integers representing the initial positions of Alice's and Bob's chips on the board, such that 1 <= x_a, x_b <= h and 1 <= y_a, y_b <= w. Additionally, x_a != x_b or y_a != y_b.
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
        
    #State: `_` is `t`, `r`, `w`, `a`, `b`, `c`, `d` are integers, stdin is empty. If `a` is greater than `c`, 'Draw' is printed. If `a` is less than or equal to `c`, either 'Draw', 'Alice', or 'Bob' is printed depending on the absolute difference between `a` and `c`, and the values of `r`, `w`, `d`, `x`, `l`, and `b`.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains six integers representing the dimensions of a board and the initial positions of Alice's and Bob's chips. It then determines the winner of a game based on the positions of the chips and prints 'Draw', 'Alice', or 'Bob' depending on the outcome. The function processes all test cases and prints the result for each case, leaving the standard input empty after execution.

