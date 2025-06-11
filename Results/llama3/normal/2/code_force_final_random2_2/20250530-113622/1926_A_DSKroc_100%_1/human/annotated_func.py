#State of the program right berfore the function call: stdin contains two inputs: first an integer (between 1 and 32) and then a series of strings of length 5 consisting of letters A and B. The number of strings is equal to the first integer.
    t = int(input())
    for q in range(t):
        ac = 0
        
        bc = 0
        
        s = input()
        
        for i in s:
            if i == 'A':
                ac += 1
            else:
                bc += 1
        
        if ac > bc:
            print('A')
        else:
            print('B')
        
    #State: t is an integer between 1 and 32, q is t-1, ac is the total number of 'A's in all input strings, bc is the total number of 'B's in all input strings, s is an empty string, stdin contains 0 inputs. If ac is greater than bc, 'A' is printed t times. Otherwise, 'B' is printed t times.

#Overall this is what the function does:This function reads a series of input strings from the standard input, each consisting of letters A and B, and prints the dominant letter ('A' or 'B') for each string. The number of input strings is determined by the first integer input, which can range from 1 to 32. The function then outputs the dominant letter for each string, either 'A' or 'B', based on the count of 'A's and 'B's in each string.

