#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: cnt is the sum of the integer parts of half of all elements in the list `a` plus 1 if all the first three elements of `a` are odd numbers, otherwise `cnt` is the sum of the integer parts of half of all elements in the list `a`, `a` is an empty list, `x` is the last element of the initial list `a`, and the value of `cnt` which is 0 is being printed.

#Overall this is what the function does:This function reads a series of lines from standard input, where each line contains four integers. For each line, it calculates a count (cnt) that is the sum of the integer parts of half of all elements in the line, plus 1 if all the first three elements are odd numbers. It then prints this count. The function processes multiple lines as specified by an initial integer input (t), repeating the calculation and printing process for each line.

