#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: The output state will be the sum of the number of times the first three elements of each line sum to an odd number and half the sum of all elements in the line, repeated for each line.

#Overall this is what the function does:The function reads a series of lines from standard input, where each line contains four integers. It then processes each line by checking if the first three integers sum to an odd number and calculates half the sum of all four integers. The function outputs the sum of these two calculations for each line, repeating the process for the specified number of lines.

