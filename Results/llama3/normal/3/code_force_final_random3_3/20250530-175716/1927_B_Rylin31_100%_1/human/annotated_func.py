#State of the program right berfore the function call: stdin contains a number of test cases, each test case contains two inputs: first an integer n and then a list of n integers.
    for i in range(int(input())):
        l = int(input())
        
        s = [(0) for i in range(l)]
        
        array = list(map(int, input().split()))
        
        ans = ''
        
        for j in array:
            ans += chr(s[j] + 97)
            s[j] += 1
        
        print(ans)
        
    #State: i is the number of test cases minus 1, l is an integer equal to the input integer, s is a list of integers with length l where the jth element is equal to the number of times j appears in the array and all other elements are 0, array is an empty list, ans is a string of length equal to the length of the array where each character is the lowercase letter corresponding to the ASCII value of 97 plus the value of the jth element in s after incrementing, j is undefined, stdin is empty, and the string "ans" containing characters 'a' through the character represented by the ASCII value 96 plus the length of the array is being printed.

#Overall this is what the function does:This function reads a number of test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then generates a string where each character corresponds to the lowercase letter represented by the ASCII value 97 plus the count of the corresponding integer in the list, and prints this string. The function repeats this process for each test case, consuming all input from standard input.

