#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif (a - b == -a, a) or (b - a == -b, b):
            print('no')
        elif (a - b) % 2 > 0 or (a - b) % 2 < 0:
            print('yes')
        else:
            print('no')
        
    #State: A sequence of 'yes' or 'no' strings, one for each pair of integers a and b read from the standard input, indicating whether the conditions in the if-elif-else statement are met for each pair.

#Overall this is what the function does:The function reads a sequence of pairs of integers from the standard input and prints a sequence of 'yes' or 'no' strings, one for each pair, indicating whether the difference between the two integers in each pair is even or odd, or if one integer is double the other.

