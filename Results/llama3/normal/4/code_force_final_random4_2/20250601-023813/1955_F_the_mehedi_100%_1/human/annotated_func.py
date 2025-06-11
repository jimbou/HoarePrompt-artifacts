#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: cnt is either 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20, a is a list of four integers that must have at least 4 elements, stdin contains t-1 lines, each containing four integers p_i (0 <= p_i <= 200), x is the fourth element in the list, and the value of cnt which is either 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 is being printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four integers. It calculates a count based on these integers, specifically incrementing the count if all four integers are odd, and then adding half of each integer to the count. The function prints the calculated count for each test case.

