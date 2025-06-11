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
        
    #State: The output state will contain the results of each test case, which will be either -1, the sum of p1 and p2, or the sum of p1, p2, and p3, depending on the conditions in the loop. The value of t will remain unchanged as it is not modified within the loop. The stdin will be empty as all the test cases have been read and processed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the scores of three players. It then processes each test case and prints the result, which can be either -1 (if the sum of the scores is odd), the sum of the first two scores (if the third score is greater than or equal to the sum of the first two), or the sum of the first and third scores (if the third score is less than the sum of the first two and certain conditions are met). The function continues this process until all test cases have been read and processed, leaving the standard input empty.

