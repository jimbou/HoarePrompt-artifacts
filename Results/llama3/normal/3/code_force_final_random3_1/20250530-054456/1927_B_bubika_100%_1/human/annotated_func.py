#State of the program right berfore the function call: stdin contains a series of inputs: the first line contains a single integer t (1 <= t <= 10^4), then for each test case, the first line contains a single integer n (1 <= n <= 2 * 10^5) and the second line contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
    a = 'abcdefghijklmnopqrstuvwxyz'
    for t in range(int(input())):
        b = [0] * 26
        
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: a is 'abcdefghijklmnopqrstuvwxyz', t is equal to the initial value of t, b is a list of 26 integers with a single value equal to the number of times the corresponding letter appears in the string r and all other values 0, n is an integer, s is an empty list, r is a string containing all the letters of the alphabet that appear in the list s in the order they appear, i is undefined, and stdin contains no input, and an empty string is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n integers. For each test case, it constructs a string r by mapping each integer in the list to a corresponding letter of the alphabet (where the first occurrence of an integer maps to 'a', the second to 'b', and so on), and prints the resulting string. The function processes all test cases and then terminates, leaving the input stream empty.

