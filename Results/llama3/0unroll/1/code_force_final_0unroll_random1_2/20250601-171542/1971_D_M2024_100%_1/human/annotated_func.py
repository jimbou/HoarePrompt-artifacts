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
        
    #State: The output state will contain t lines, each containing a single integer. The integer on each line will be the total number of cuts required to make all the '1's and '0's in the corresponding input string s alternate. If the string already has alternating '1's and '0's, the output will be 1. If the string has only '0's or only '1's, the output will be the number of '1's or '0's in the string plus 1.

#Overall this is what the function does:This function reads a series of binary strings from standard input, calculates the minimum number of cuts required to make the '1's and '0's in each string alternate, and prints the results. If a string already has alternating '1's and '0's, it outputs 1. If a string consists of only '0's or only '1's, it outputs the number of '1's or '0's in the string plus 1. The function processes multiple strings, with the number of strings specified by the first input, and outputs the results for each string on a separate line.

