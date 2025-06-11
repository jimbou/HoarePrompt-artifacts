#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: The output will be a series of integers, each representing the result of the calculation for the corresponding input line. The calculation involves checking if the first three numbers in the line are odd (i.e., their remainder when divided by 2 is 1), and if so, adding 1 to the sum of the numbers in the line divided by 2. If the first three numbers are not all odd, the result is simply the sum of the numbers in the line divided by 2.

#Overall this is what the function does:This function reads a series of lines from standard input, where each line contains four integers. For each line, it checks if the first three integers are odd, and if so, adds 1 to the sum of all four integers divided by 2. If the first three integers are not all odd, it simply calculates the sum of all four integers divided by 2. The function then prints the result of this calculation for each input line.

