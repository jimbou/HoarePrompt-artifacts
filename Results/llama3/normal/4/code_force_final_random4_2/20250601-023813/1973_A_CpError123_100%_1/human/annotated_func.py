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
        
    #State: t is 0, _ is t, a, b, and c are integers (0 <= a <= b <= c <= 30) and are equal to p_1, p_2 and p_3 respectively, x is an integer equal to the sum of a, b, and c divided by 2, y is an integer equal to the sum of a and b, stdin is empty, and the minimum of x and y is printed, where x is the sum of a, b, and c divided by 2 and y is the sum of a and b.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains three integers representing the scores of three players. It calculates the minimum of two values: the sum of the scores divided by 2, and the sum of the scores of the first two players. If the sum of the scores is odd, it prints -1. Otherwise, it prints the calculated minimum value. The function processes all test cases and leaves the standard input empty.

