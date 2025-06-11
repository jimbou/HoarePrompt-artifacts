#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: The results of the calculation for each input line, one per line

#Overall this is what the function does:Reads a series of input lines from standard input, where the first line contains an integer t, and each of the following t lines contains four integers. For each line of four integers, calculates a value by summing the result of a formula applied to each integer, and prints the result of this calculation, divided by 3, one result per line.

