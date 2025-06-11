#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains six integers: h, w, x_a, y_a, x_b, y_b. h and w are positive integers, 1 <= x_a, x_b <= h, 1 <= y_a, y_b <= w. x_a is not equal to x_b or y_a is not equal to y_b.
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
        
    #State: The output state after the loop executes all the iterations will be a list of strings, where each string is either 'Draw', 'Alice', or 'Bob'. The number of strings in the list will be equal to the number of test cases (t). Each string will be the result of the game for the corresponding test case, based on the rules defined in the loop body. The values of the variables t, h, w, x_a, y_a, x_b, and y_b will remain unchanged.

#Overall this is what the function does:Determines the winner of a game for multiple test cases, where each test case involves two players, Alice and Bob, with their respective positions on a grid. The function takes no arguments and returns a list of strings, where each string represents the result of a test case, either 'Draw', 'Alice', or 'Bob', based on the rules defined in the loop body. The function processes the input test cases from standard input and prints the results to standard output.

