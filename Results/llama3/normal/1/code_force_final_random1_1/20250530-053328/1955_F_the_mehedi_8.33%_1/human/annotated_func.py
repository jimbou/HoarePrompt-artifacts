#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] == a[1] == a[2] and a[0] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: The loop has finished executing, and the output state is the sum of the integer divisions of each element in `a` by 2, which is `cnt`.

#Overall this is what the function does:This function reads a series of lines from standard input, where each line contains four integers. For each line, it calculates the sum of the integer divisions of each element by 2, and adds 1 to the sum if all four elements are equal and odd. The function then prints this sum for each line.

