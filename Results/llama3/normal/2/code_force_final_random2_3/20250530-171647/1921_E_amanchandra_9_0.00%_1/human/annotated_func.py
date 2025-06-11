#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains six integers h, w, x_a, y_a, x_b, y_b (1 <= x_a, x_b <= h <= 10^6, 1 <= y_a, y_b <= w <= 10^9) — the dimensions of the board and the initial positions of Alice's and Bob's chips. It is guaranteed that either x_a != x_b or y_a != y_b.
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
        
    #State: The loop has executed for all test cases in the input, and the output for each test case has been printed. The values of `h`, `w`, `xa`, `ya`, `xb`, and `yb` are the last 6 integers from the input. If `xa` is greater than `xb`, 'Draw' is printed. If `xa` is less than or equal to `xb`, `x` is the absolute difference between `xa` and `xb` divided by 2. If the absolute difference between `xa` and `xb` is odd, either 'Draw' or 'Alice' is printed based on the conditions `abs(l - ya) <= x + 1` and `abs(r - ya) <= x + 1`, where `l` is the maximum of 1 and `yb - x`, and `r` is the minimum of `w` and `yb + x`. If the absolute difference between `xa` and `xb` is even, either 'Draw' or 'Bob' is printed based on the conditions `abs(l - yb) <= x` and `abs(r - yb) <= x`, where `l` is the maximum of 1 and `ya - x`, and `r` is the minimum of `w` and `ya + x`.

#Overall this is what the function does:This function determines the winner of a game between Alice and Bob based on their initial positions on a board. It takes six integers as input: the dimensions of the board (h and w) and the initial positions of Alice's and Bob's chips (xa, ya, xb, and yb). The function then prints 'Draw' if Alice's x-coordinate is greater than Bob's, or determines the winner based on the difference between their x-coordinates and the distance between their y-coordinates. If the difference between their x-coordinates is odd, the function checks if Alice can reach Bob's y-coordinate within a certain distance, and if so, prints 'Alice'. If the difference is even, the function checks if Bob can reach Alice's y-coordinate within a certain distance, and if so, prints 'Bob'. Otherwise, it prints 'Draw'. The function processes multiple test cases from standard input and prints the result for each case.

