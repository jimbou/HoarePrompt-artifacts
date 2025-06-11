#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: The output state will be the sum of the counts for each iteration of the loop. The count for each iteration is the sum of the number of odd numbers in the input list and the sum of the integer divisions of each number in the list by 2.

#Overall this is what the function does:This function reads a series of lines from standard input, where each line contains four integers. It calculates a count for each line by adding the number of odd integers in the line to the sum of the integer divisions of each integer by 2. The function then prints the count for each line.

