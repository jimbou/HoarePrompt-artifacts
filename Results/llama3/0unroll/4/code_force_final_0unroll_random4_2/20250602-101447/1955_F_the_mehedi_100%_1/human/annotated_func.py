#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: The output state will contain t lines, each containing an integer that represents the total count of numbers that are either odd or can be divided by 2. The count is calculated for each set of four integers p_i.

#Overall this is what the function does:This function reads a series of sets of four integers from standard input, calculates the total count of numbers that are either odd or can be divided by 2 for each set, and prints the counts. It processes multiple sets based on an initial input specifying the number of sets.

