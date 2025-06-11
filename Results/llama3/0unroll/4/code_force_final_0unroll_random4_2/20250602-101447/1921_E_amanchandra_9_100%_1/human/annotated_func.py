#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 10^4) — the number of test cases. Each test case consists of a single line containing six integers h, w, x_a, y_a, x_b, y_b (1 <= x_a, x_b <= h <= 10^6, 1 <= y_a, y_b <= w <= 10^9) — the dimensions of the board and the initial positions of Alice's and Bob's chips. It is guaranteed that either x_a != x_b or y_a != y_b.
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
        
    #State: The output state will be a list of strings, where each string is either 'Draw', 'Alice', or 'Bob', depending on the values of the input variables r, w, a, b, c, and d. The number of strings in the list will be equal to the value of t. The state of the variable t will be unchanged.

#Overall this is what the function does:Determines the winner of a game between Alice and Bob based on their initial positions on a board and prints the result for each test case. The function takes no parameters and returns a list of strings indicating the winner ('Alice', 'Bob', or 'Draw') for each test case. The number of test cases is determined by the input value 't'.

