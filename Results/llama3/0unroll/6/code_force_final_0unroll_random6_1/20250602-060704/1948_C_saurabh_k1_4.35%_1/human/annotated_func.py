#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: the first input is an integer (2 <= n <= 2 * 10^5), the second input is a string of n characters (< and/or >), and the third input is a string of n characters (< and/or >).
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: The output state will be a series of 'Yes' or 'No' printed for each test case, indicating whether the condition was met or not. The number of outputs will be equal to the number of test cases provided in the input.

#Overall this is what the function does:This function evaluates multiple test cases from standard input and prints 'Yes' or 'No' for each case, indicating whether the second-to-last character of the third input string is not '<'. The function processes each test case independently and does not modify the input data.

