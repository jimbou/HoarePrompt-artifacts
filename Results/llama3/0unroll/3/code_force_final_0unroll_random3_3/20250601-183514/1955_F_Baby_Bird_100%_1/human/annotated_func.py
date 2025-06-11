#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: the sum of the weighted values of four integers p_i for each of t lines, where the weight is 3 for the first two integers and 1 for the last two integers, divided by 3

#Overall this is what the function does:The function reads a series of lines from standard input, where the first line contains an integer t, representing the number of subsequent lines. Each of the subsequent lines contains four integers. The function calculates a weighted sum for each line, where the first two integers are weighted by 3 and the last two integers are weighted by 1. The weighted sum is then divided by 3. The function prints the results of these calculations for each line, one result per line.

