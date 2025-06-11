#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings, each consisting of characters '0' and '1' with length between 1 and 500.
    t = int(input())
    for _ in range(t):
        a = input()
        
        cut = 0
        
        for i in range(len(a) - 1):
            if a[i] == '1' and a[i + 1] == '0':
                cut += 1
        
        print(cut + 1)
        
    #State: t is 0, stdin is empty, a is the last string consisting of characters '0' and '1' with length between 1 and 500, cut is the number of times '1' is followed by '0' in the last string a, i is len(a) - 2, _ is t-1, and the number of times '1' is followed by '0' in each string plus 1 has been printed.

#Overall this is what the function does:This function reads a series of binary strings from standard input, counts the number of occurrences of '1' followed by '0' in each string, and prints the count plus one for each string. It continues this process until all input strings have been processed, at which point the standard input is empty.

