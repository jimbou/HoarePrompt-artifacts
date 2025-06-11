#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings s (1 <= |s| <= 500) consisting of characters 0 and 1.
    t = int(input())
    for _ in range(t):
        a = input()
        
        cut = 0
        
        for i in range(len(a) - 1):
            if a[i] == '1' and a[i + 1] == '0':
                cut += 1
        
        print(cut + 1)
        
    #State: The output state will be a list of integers, each representing the number of cuts required to split the corresponding input string into substrings of consecutive 1's and 0's. The length of the output list will be equal to the value of `t`.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t strings consisting of characters 0 and 1. It then calculates the minimum number of cuts required to split each string into substrings of consecutive 1's and 0's, and prints the results as a list of integers. The length of the output list is equal to the value of t.

