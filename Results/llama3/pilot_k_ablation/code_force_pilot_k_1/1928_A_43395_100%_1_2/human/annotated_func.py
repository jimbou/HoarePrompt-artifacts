#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif a % 2 == 0 and a / 2 != b or b % 2 == 0 and b / 2 != a:
            print('yes')
        else:
            print('no')
        
    #State: stdin is empty, a and b are the last pair of integers between 1 and 10^9 read from stdin, i is equal to the number of pairs of integers read from stdin minus 1.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, determines whether each pair meets certain parity conditions, and prints 'yes' if the conditions are met and 'no' otherwise. The function processes all input pairs and empties the standard input buffer, leaving the last pair of integers and the number of processed pairs as the final state.

