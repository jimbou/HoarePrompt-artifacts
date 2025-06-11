#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] == a[1] == a[2] and a[0] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200), and the printed counts for each line.

#Overall this is what the function does:The function reads a series of lines from standard input, where each line contains four integers. It then calculates and prints the count of pairs of integers that can be formed from these four integers, considering all possible pairs and counting each pair only once. The function repeats this process for a specified number of lines, as indicated by an initial integer input.

