#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by 2t strings x and y, each consisting of digits from 1 to 9 and of the same length.
    for _ in range(int(input())):
        a = list(map(int, list(input())))
        
        b = list(map(int, list(input())))
        
        new = [None] * len(a)
        
        new2 = [None] * len(a)
        
        i = 0
        
        while i < len(a) and a[i] == b[i]:
            new[i] = max(a[i], b[i])
            new2[i] = min(a[i], b[i])
            i += 1
        
        if i != len(a):
            new[i] = max(a[i], b[i])
            new2[i] = min(a[i], b[i])
            i += 1
            while i < len(a):
                new[i] = min(a[i], b[i])
                new2[i] = max(a[i], b[i])
                i += 1
        
        print(''.join(str(x) for x in new))
        
        print(''.join(str(x) for x in new2))
        
    #State: The output state contains 2t strings, each consisting of digits from 1 to 9 and of the same length as the input strings. The strings are the result of comparing the corresponding characters of the input strings x and y, and printing the maximum and minimum values for each pair of characters. If the characters at the first mismatched position are different, the remaining characters in the strings are swapped.

#Overall this is what the function does:The function takes as input a series of pairs of strings consisting of digits from 1 to 9, compares the corresponding characters of each pair, and prints two new strings for each pair. The first string contains the maximum value for each pair of characters, and the second string contains the minimum value for each pair of characters. If the characters at the first mismatched position are different, the remaining characters in the strings are swapped. The function repeats this process for a number of pairs specified by the input, and produces a total of 2t output strings, where t is the number of pairs.

