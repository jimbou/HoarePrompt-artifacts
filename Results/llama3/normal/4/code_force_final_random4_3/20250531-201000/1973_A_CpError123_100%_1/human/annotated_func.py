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
        
    #State: t is 0, a, b, and c are the last integers from the input, x is the integer part of the average of the last a, b, and c, y is the sum of the last a and b, stdin contains no input, and the minimum value between the integer part of the average of the last a, b, and c and the sum of the last a and b is printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. It calculates the minimum value between the integer part of the average of the three scores and the sum of the first two scores for each test case, and prints this value. If the sum of the three scores is odd, it prints -1 for that test case. After processing all test cases, the function leaves the input stream empty.

