#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings s (1 <= |s| <= 500) consisting of characters '0' and '1'.
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
        
    #State: The output state will contain t lines, each representing the number of cuts required to make the string alternating. If the string is already alternating, the output will be the number of cuts required to make it non-alternating. If the string is not alternating, the output will be the total number of cuts required to make it alternating.

#Overall this is what the function does:This function reads a series of binary strings from standard input and calculates the minimum number of cuts required to make each string alternating. If a string is already alternating, it calculates the number of cuts needed to make it non-alternating. The function then prints the result for each string on a new line.

