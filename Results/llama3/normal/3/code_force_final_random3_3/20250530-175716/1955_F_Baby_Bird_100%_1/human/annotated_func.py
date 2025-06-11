#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: The sum of the weighted values of four integers for each line of input, where the weights are 3 times the integer divided by 2 plus the remainder of the integer divided by 2 if the integer is in the first three positions, and the sum is divided by 3, repeated for the number of lines specified by the first integer input.

#Overall this is what the function does:The function reads an integer t from standard input, representing the number of lines to process. It then reads t lines, each containing four integers. For each line, it calculates a weighted sum of the integers, where the first three integers are weighted 3 times their integer division by 2 plus their remainder when divided by 2, and the fourth integer is not weighted. The sum is then divided by 3. The function prints the calculated weighted sum for each line, separated by newline characters.

