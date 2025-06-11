#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 32) followed by t strings of length 5 consisting of letters A and B.
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
        
    #State: The program will print 'A' for each string where the count of 'A's is greater than the count of 'B's, and 'B' otherwise. The value of `t` remains unchanged.

#Overall this is what the function does:The function reads an integer t from standard input, representing the number of strings to process. It then reads t strings of length 5, each consisting of letters A and B. For each string, it counts the occurrences of 'A' and 'B', and prints 'A' if the count of 'A's is greater than the count of 'B's, and 'B' otherwise. The function does not modify the input value of t.

