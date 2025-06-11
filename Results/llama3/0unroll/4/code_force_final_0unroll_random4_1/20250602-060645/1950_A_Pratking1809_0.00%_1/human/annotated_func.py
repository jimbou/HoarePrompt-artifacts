#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three digits a, b, c (0 <= a, b, c <= 9).
    q = int(input())
    mn = 100
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        
        if a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: Output State: The loop has executed q times, and for each iteration, it has printed one of the strings 'STAIR', 'PEAK', or 'NONE' to the standard output, depending on the values of a, b, and c read from the standard input. The values of q and mn remain unchanged.

#Overall this is what the function does:This function reads an integer t from standard input, representing the number of test cases, and then for each test case, it reads three digits a, b, and c. Based on the values of a, b, and c, it prints one of the strings 'STAIR', 'PEAK', or 'NONE' to the standard output, indicating whether the digits form a stair, peak, or none of these patterns, respectively. The function does not modify the input values or return any values, only producing output based on the input patterns.

