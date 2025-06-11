#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains a single integer t (1 <= t <= 10^4) — the number of test cases. Each test case consists of a single line containing six integers h, w, x_a, y_a, x_b, y_b (1 <= x_a, x_b <= h <= 10^6, 1 <= y_a, y_b <= w <= 10^9) — the dimensions of the board and the initial positions of Alice's and Bob's chips. It is guaranteed that either x_a != x_b or y_a != y_b.
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
        
    #State: _ is t, t is an integer between 0 and 10^4 (exclusive), r, w, a, b, c, and d are integers assigned from the input, stdin contains no test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of six integers representing the dimensions of a board and the initial positions of two chips, Alice's and Bob's. It then determines the winner of a game based on the relative positions of the chips and prints the result, either 'Alice', 'Bob', or 'Draw', for each test case. The function processes all test cases and consumes all input from standard input, leaving it empty.

