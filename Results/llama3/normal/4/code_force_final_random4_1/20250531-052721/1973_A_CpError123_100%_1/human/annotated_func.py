#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers p_1, p_2 and p_3 (0 <= p_1 <= p_2 <= p_3 <= 30) — the scores of the three players, sorted non-decreasingly.
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        if (a + b + c) % 2 != 0:
            print(-1)
            continue
        
        x = (a + b + c) // 2
        
        y = a + b
        
        print(min(x, y))
        
    #State: t is 0, a, b, and c are integers from the input, x is an integer equal to half the sum of a, b, and c, y is an integer equal to the sum of a and b, _ is t, and the minimum value between x and y is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. It calculates the minimum value between half the sum of the scores and the sum of the first two scores, and prints this value. If the sum of the scores is odd, it prints -1 instead. The function processes all test cases and does not return any value.

