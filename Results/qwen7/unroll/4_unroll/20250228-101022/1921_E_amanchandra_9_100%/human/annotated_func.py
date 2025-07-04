#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of six positive integers h, w, x_a, y_a, x_b, y_b such that 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9. It is guaranteed that either x_a ≠ x_b or y_a ≠ y_b, and the sum of h over all test cases does not exceed 10^6.
def func():
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
        
    #State: Output State: The output state will consist of a series of lines, each containing either 'Draw', 'Alice', or 'Bob', depending on the input values for each iteration of the loop. For each input set (r, w, a, b, c, d), the program compares a and c. If a is greater than c, it prints 'Draw'. Otherwise, it calculates x as half the absolute difference between a and c, then determines whether Alice or Bob wins based on the positions b and d relative to the calculated range.
#Overall this is what the function does:The function processes a series of test cases, each consisting of six positive integers \(h\), \(w\), \(x_a\), \(y_a\), \(x_b\), and \(y_b\). For each test case, it compares \(x_a\) and \(x_b\). If \(x_a\) is greater than \(x_b\), it prints 'Draw'. Otherwise, it calculates a value \(x\) as half the absolute difference between \(x_a\) and \(x_b\). Depending on the positions of \(b\) and \(d\) relative to \(x\), it determines whether 'Alice' or 'Bob' wins and prints the corresponding result ('Draw', 'Alice', or 'Bob'). The function does not return any value but outputs the results for each test case.

