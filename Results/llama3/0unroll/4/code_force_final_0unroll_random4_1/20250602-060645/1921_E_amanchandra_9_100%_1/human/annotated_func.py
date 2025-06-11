#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains six integers h, w, x_a, y_a, x_b, y_b such that 1 <= x_a, x_b <= h <= 10^6 and 1 <= y_a, y_b <= w <= 10^9. The first integer in stdin is the number of test cases (1 <= t <= 10^4).
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
        
    #State: The output state will be a list of strings, where each string is either 'Draw', 'Alice', or 'Bob', indicating the winner of each game. The length of the list will be equal to the value of `t`. The values of `h`, `w`, `x_a`, `y_a`, `x_b`, and `y_b` will remain unchanged.

#Overall this is what the function does:Determines the winner of a game for multiple test cases, where each test case consists of six integers representing the height and width of a grid, and the positions of two players, Alice and Bob. The function takes no parameters and returns a list of strings indicating the winner of each game, either 'Draw', 'Alice', or 'Bob', based on the relative positions of the players. The function processes multiple test cases from standard input and outputs the results in the same order.

