#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 ≤ t ≤ 32), and the remaining t inputs are strings of length 5 consisting of letters A and B.
    t = int(input())
    l = 0
    h = 0
    for i in range(t):
        a = str(input())
        
        for j in a:
            if j in 'A':
                l += 1
            else:
                h += 1
        
        if l > h:
            print('A')
        elif l < h:
            print('B')
        
    #State: `t` is an integer between 1 and 32 (inclusive), `l` is 0, `h` is 0, stdin contains 0 input strings of length 5 consisting of letters A and B.

#Overall this is what the function does:This function reads a series of input strings from stdin, each of length 5 consisting of letters A and B, and prints 'A' if the count of 'A's is greater than the count of 'B's, 'B' if the count of 'B's is greater than the count of 'A's, and does not print anything if the counts are equal. The function processes a number of input strings specified by the first input, an integer between 1 and 32 (inclusive). After processing all input strings, the function leaves the input variables in their initial state, with no remaining input strings in stdin.

