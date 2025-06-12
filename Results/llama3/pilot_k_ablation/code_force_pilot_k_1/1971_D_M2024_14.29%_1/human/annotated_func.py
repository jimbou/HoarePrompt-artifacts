#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings, each consisting of characters '0' and '1' with length between 1 and 500.
    t = int(input())
    for _ in range(t):
        a = input()
        
        cut = 0
        
        for i in range(len(a) - 1):
            if a[i] == '1' and a[i + 1] == '0':
                cut += 1
        
        print(cut + 1)
        
    #State: `t` is 0, `stdin` is empty, `_` is `t`, `a` is the last string consisting of characters '0' and '1' with length between 1 and 500 that was read from `stdin`, `cut` is the number of occurrences of '10' in the last string `a` that was read from `stdin`.

#Overall this is what the function does:Reads a specified number of binary strings from standard input, counts the occurrences of the substring '10' in each string, and prints the count plus one for each string.

