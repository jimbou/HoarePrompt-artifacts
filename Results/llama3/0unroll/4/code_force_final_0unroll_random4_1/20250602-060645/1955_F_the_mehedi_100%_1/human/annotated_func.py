#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: The output state will contain t lines, each containing an integer cnt. The value of cnt for each line is calculated based on the input values of a. If all elements of a are odd, cnt is incremented by 1. Then, for each element x in a, cnt is incremented by the integer division of x by 2. The final value of cnt is printed for each iteration of the loop.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four integers. For each test case, it calculates a count based on the input values: if all four integers are odd, it increments the count by 1, and then adds the integer division of each input value by 2 to the count. The function prints the calculated count for each test case.

