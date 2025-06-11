#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three space-separated integers p_1, p_2 and p_3 (0 <= p_1 <= p_2 <= p_3 <= 30).
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
        
    #State: `t` is a positive integer that must be at least 0, `p1`, `p2`, and `p3` are integers where 0 <= `p1` <= `p2` <= `p3` <= 30, stdin contains multiple test cases minus `t` test cases. If the sum of `p1`, `p2`, and `p3` is odd, -1 is printed and we move on to the next iteration of the loop. Otherwise, if `p3` is greater than or equal to the sum of `p1` and `p2`, the sum of `p1` and `p2` is printed. Otherwise, the program continues with the next operation. If the difference between `p1` and `cur` is less than or equal to the difference between `p2` and the difference between `p3` and `cur`, then `p1 - cur + p3` is printed. Otherwise, `cur` is incremented by 1 and equals to `high`.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers p1, p2, and p3. It then processes each test case based on the following rules: If the sum of p1, p2, and p3 is odd, it prints -1 and moves on to the next test case. If p3 is greater than or equal to the sum of p1 and p2, it prints the sum of p1 and p2. Otherwise, it performs a binary search-like operation to find the maximum possible value that can be obtained by subtracting a certain value from p1 and adding p3, and prints this value. If no such value is found, it prints p3. The function continues this process until all test cases have been processed.

