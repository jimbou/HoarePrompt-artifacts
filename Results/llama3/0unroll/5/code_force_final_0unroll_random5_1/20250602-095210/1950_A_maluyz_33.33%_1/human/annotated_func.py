#State of the program right berfore the function call: stdin contains two inputs: first an integer (between 1 and 1000) and then a sequence of lines, each containing three digits (between 0 and 9).
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a == b == c:
            print('NONE')
        elif max(a, b, c) == b:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The output state will contain 't' number of lines, each containing one of the strings 'STAIR', 'NONE', or 'PEAK'. The value of 't' remains unchanged. The stdin will be empty as all the lines have been read by the loop.

#Overall this is what the function does:This function reads a sequence of integer inputs from standard input, where the first input is the number of test cases (t) and each subsequent input is a sequence of three digits. It then classifies each sequence of three digits into one of four categories: 'STAIR' if the digits are in ascending order, 'NONE' if they are not in ascending order and the middle digit is not the maximum, 'PEAK' if the middle digit is the maximum, and 'NONE' if all digits are equal. The function prints the classification for each sequence of three digits, resulting in 't' number of output lines.

