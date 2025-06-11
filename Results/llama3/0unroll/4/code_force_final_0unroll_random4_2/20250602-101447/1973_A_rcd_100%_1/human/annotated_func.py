#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). Each test case contains three integers p_1, p_2 and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) — the scores of the three players, sorted non-decreasingly.
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
        
    #State: The output state will contain the results of the loop's executions, which are the number of test cases that were processed. For each test case, the output will be either -1 (if the sum of p1, p2, and p3 is odd), the sum of p1 and p2 (if p3 is greater than or equal to the sum of p1 and p2), or the result of the while loop (if p3 is less than the sum of p1 and p2). The output state will not contain the values of t, p1, p2, or p3, as they are only used within the loop and do not affect the overall state of the program.

#Overall this is what the function does:This function processes multiple test cases from standard input, each containing three sorted integers representing player scores. It calculates and prints the result for each test case, which can be -1 if the sum of scores is odd, the sum of the first two scores if the third score is greater than or equal to their sum, or the result of a specific iterative calculation if the third score is less than the sum of the first two scores. The function does not return any value but prints the results for all test cases.

