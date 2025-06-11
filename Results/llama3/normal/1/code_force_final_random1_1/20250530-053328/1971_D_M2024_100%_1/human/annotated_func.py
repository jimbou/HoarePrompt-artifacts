#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings, each consisting of characters '0' and '1' with length between 1 and 500 (inclusive).
    t = int(input())
    for _ in range(t):
        a = input()
        
        cut0 = 0
        
        cut1 = 0
        
        for i in range(len(a) - 1):
            if a[i] == '1' and a[i + 1] == '0':
                cut1 += 1
            if a[i] == '0' and a[i + 1] == '1':
                cut0 += 1
        
        if cut0 == 0:
            print(cut1 + 1)
        else:
            print(cut0 + cut1)
        
    #State: `a` is a string of '0's and '1's with length between 1 and 500 (inclusive), `cut0` is the number of times '0' is followed by '1' in `a`, `cut1` is the number of times '1' is followed by '0' in `a`, `i` is `len(a) - 1`, `_` is `t-1`, `t` is not defined, stdin contains 0 strings. If `cut0` is 0, the value of `cut1 + 1` is printed. Otherwise, the sum of `cut0` and `cut1` is printed.

#Overall this is what the function does:This function reads a series of binary strings from standard input, counts the number of transitions from 0 to 1 and from 1 to 0 in each string, and prints the total number of transitions plus one if there are no transitions from 0 to 1, otherwise it prints the total number of transitions.

