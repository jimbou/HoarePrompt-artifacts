#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] == a[1] == a[2] and a[0] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: The total number of times the counter was incremented, which is the sum of the counters for each line.

#Overall this is what the function does:This function reads a series of lines from standard input, where each line contains four integers. It then calculates and prints the total number of times a counter can be incremented based on the values in each line. The counter is incremented if the first three integers are the same and odd, and also for each integer in the line, the counter is incremented by half of the integer's value. The function repeats this process for a number of lines specified by the first integer read from standard input.

