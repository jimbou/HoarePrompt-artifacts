#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains an integer n. The second line contains a list of n integers a_1, a_2, ..., a_n.
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = [0] * 26
    for t in range(int(input())):
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: a remains 'abcdefghijklmnopqrstuvwxyz', b's values are incremented based on the indices used from input lists s, and multiple strings r are printed based on the mapping of indices to characters in a.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It maps each integer in the list to a character in the alphabet (a-z) based on its index, increments the corresponding index in a tracking list, and prints the resulting string. The function repeats this process for all test cases, producing multiple output strings.

