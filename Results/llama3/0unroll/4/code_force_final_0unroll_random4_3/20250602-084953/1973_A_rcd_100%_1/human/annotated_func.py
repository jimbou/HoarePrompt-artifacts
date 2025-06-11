#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers p_1, p_2 and p_3 (0 <= p_1 <= p_2 <= p_3 <= 30) — the scores of the three players, sorted non-decreasingly.
    t = int(input())
    for _ in range(t):
        p1, p2, p3 = map(int, input().split())
        
        if (p1 + p2 + p3) % 2 != 0:
            print(-1)
            continue
        
        if p3 >= p1 + p2:
            print(p1 + p2)
        else:
            x = 0
            y = p3
            while y >= x:
                if p1 - x <= p2 - y:
                    print(p1 - x + p3)
                    break
                else:
                    x += 1
                    y -= 1
            else:
                print(p3)
        
    #State: The output state will be a series of integers, each representing the maximum possible score that can be achieved by the three players in each test case, or -1 if it is not possible to achieve a score that is a multiple of 2. The number of integers in the output state will be equal to the number of test cases minus one.

#Overall this is what the function does:This function processes multiple test cases from standard input, each containing three integers representing the scores of three players. It calculates and prints the maximum possible score that can be achieved by the players in each test case, or -1 if it's not possible to achieve a score that is a multiple of 2. The function handles cases where the sum of the scores is odd, where the third player's score is greater than or equal to the sum of the first two players' scores, and where the scores need to be adjusted to achieve the maximum possible score. The output is a series of integers, each representing the maximum possible score for each test case.

