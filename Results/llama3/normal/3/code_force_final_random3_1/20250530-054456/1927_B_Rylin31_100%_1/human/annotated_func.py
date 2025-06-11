#State of the program right berfore the function call: stdin contains a series of test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2 * 10^5) and then a list of n integers a_1, a_2, ..., a_n (0 <= a_i < n).
    for i in range(int(input())):
        l = int(input())
        
        s = [(0) for i in range(l)]
        
        array = list(map(int, input().split()))
        
        ans = ''
        
        for j in array:
            ans += chr(s[j] + 97)
            s[j] += 1
        
        print(ans)
        
    #State: i is the number of test cases minus 1, l is a positive integer equal to the input integer, s is a list of l integers where each element is equal to the number of times its index appears in array, array is an empty list, ans is a string containing the characters 'a' through 'z' repeated a number of times equal to the number of times each index appears in array, stdin is empty, j is the last element in the last array, and the string ans is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then generates a string by iterating over the list of integers, where each integer corresponds to a character in the alphabet (with 'a' corresponding to 0, 'b' to 1, and so on). The function repeats this process for each test case, printing the resulting string for each case. The function does not return any value, but rather prints the results directly to standard output.

