#State of the program right berfore the function call: stdin contains a number of test cases t, followed by t test cases. Each test case consists of two lines: the first line contains an integer n, and the second line contains n integers a_1, a_2, ..., a_n. 1 <= t <= 10^4, 1 <= n <= 2 * 10^5, 0 <= a_i < n.
    for i in range(int(input())):
        l = int(input())
        
        s = [(0) for i in range(l)]
        
        array = list(map(int, input().split()))
        
        ans = ''
        
        for j in array:
            ans += chr(s[j] + 97)
            s[j] += 1
        
        print(ans)
        
    #State: i is t-1, l is an integer, s is a list of l integers where the jth element is the number of times j appears in the array and the rest are 0, array is a list of integers, ans is a string of length equal to the length of the array containing the characters 'a' to 'z' repeated as necessary, j is the last integer in the array, and the string ans is being printed.

#Overall this is what the function does:The function reads a number of test cases from standard input, where each test case consists of an integer n followed by n integers. It then generates a string of length n by mapping each integer to a character 'a' to 'z' (repeating as necessary) based on the number of times the integer appears in the array. The function prints the generated string for each test case.

