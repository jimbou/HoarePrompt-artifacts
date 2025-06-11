#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 500). Each test case contains three integers p_1, p_2 and p_3 (0 <= p_1 <= p_2 <= p_3 <= 30) — the scores of the three players, sorted non-decreasingly.
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        if (a + b + c) % 2 != 0:
            print(-1)
            continue
        
        x = (a + b + c) // 2
        
        y = a + b
        
        print(min(x, y))
        
    #State: The loop has executed t times, and for each iteration, it has printed the minimum of x and y, where x is half of the sum of a, b, and c, and y is the sum of a and b. The value of t has been decremented to 0, and the stdin contains no more test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. For each test case, it calculates the minimum of two values: half of the total score and the sum of the scores of the first two players. If the total score is odd, it prints -1. Otherwise, it prints the calculated minimum value. The function continues this process until all test cases have been processed, at which point it terminates, leaving the standard input empty.

