#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: cnt is either 0 or 1 plus the integer division of the first integer in the list a by 2, plus the integer division of the second integer in the list a by 2, plus the integer division of the third integer in the list a by 2, plus the integer division of the fourth integer in the list a by 2, a is an empty list, x is the fourth integer in the list a, stdin contains 0 lines, and cnt is printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four integers. For each test case, it calculates a count based on the parity of the integers and their integer divisions by 2. The count is then printed to the console. The function processes all test cases and does not return any value.

