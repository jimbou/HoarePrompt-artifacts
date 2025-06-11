#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters and having a length of at most 10.
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: stdin is empty, s is a string consisting of lowercase English letters and having a length of at most 10, s2 is a string consisting of the same characters as s but in a random order. If s is not equal to s2, 'Yes' is printed along with s2. Otherwise, 'No' is printed.

#Overall this is what the function does:This function reads a series of strings from standard input, generates a random permutation of each string, and prints 'Yes' along with the permuted string if it is different from the original, or 'No' otherwise. The function processes multiple strings as specified by an initial integer input, and it empties the standard input buffer in the process.

