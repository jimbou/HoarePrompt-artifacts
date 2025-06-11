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
        
    #State: The output state after the loop executes all the iterations will be a list of strings, where each string is either 'Draw', 'Alice', or 'Bob', indicating the winner of each test case. The number of strings in the list will be equal to the number of test cases, which is the value of the variable t in the initial state.

#Overall this is what the function does:Determines the winner of a game for multiple test cases, where each test case involves two players, Alice and Bob, with chips placed on a rectangular board. The function takes no parameters but reads input from stdin, which contains the number of test cases and the dimensions of the board along with the initial positions of Alice's and Bob's chips for each test case. It then analyzes the positions to determine the winner of each test case, printing 'Draw' if the game is a draw, 'Alice' if Alice wins, or 'Bob' if Bob wins. The output is a list of strings, where each string represents the winner of a test case.

