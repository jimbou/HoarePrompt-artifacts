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
            low, high = min(p3 - p1, p3 - p2), max(p3 - p1, p3 - p2)
            cur = low
            while high >= cur:
                if p1 - cur <= p2 - (p3 - cur):
                    print(p1 - cur + p3)
                    break
                else:
                    cur += 1
            else:
                print(p3)
        
    #State: The loop will execute t-1 times, and for each iteration, it will print the result of the calculation based on the input values p1, p2, and p3. The output will be either -1, p1 + p2, or a value calculated by the while loop. The value of t will be decremented by 1 after each iteration, and the final output state will have t = 1.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. It then calculates and prints the result for each test case based on the scores. If the sum of the scores is odd, it prints -1. If the highest score is greater than or equal to the sum of the other two scores, it prints the sum of the two lower scores. Otherwise, it performs a calculation using a while loop to determine the result, which is either the highest score or a calculated value. The function continues this process until all test cases have been processed, printing a result for each one.

