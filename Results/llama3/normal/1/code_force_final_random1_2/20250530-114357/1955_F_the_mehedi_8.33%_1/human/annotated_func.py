#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] == a[1] == a[2] and a[0] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: cnt is the sum of math.floor(x / 2) for all elements in a plus 1 if the first three elements of a are equal and odd, otherwise cnt is the sum of math.floor(x / 2) for all elements in a, and the value of cnt is being printed.

#Overall this is what the function does:This function reads a series of lines from standard input, where each line contains four integers. For each line, it calculates a count (cnt) by summing the integer division of each number by 2. If the first three numbers are equal and odd, it increments the count by 1. The function then prints the calculated count for each line.

