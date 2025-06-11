#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 5000) followed by t test cases. Each test case contains an integer n (1 ≤ n ≤ 50) followed by 2n integers a_1,a_2,...,a_{2n} (1 ≤ a_i ≤ 10^7).
    numCases = int(input())
    for i in range(numCases):
        numInteger = int(input())
        
        numbers = input().split()
        
        numbers.sort(reverse=False)
        
        suma = 0
        
        while numbers != []:
            a = int(numbers.pop(0))
            b = int(numbers.pop(0))
            suma += min(a, b)
        
        print(suma)
        
    #State: The loop will print the sum of the minimum of each pair of integers in each test case, for a total of `numCases` outputs. The value of `numCases` remains unchanged.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the sum of the minimum of each pair of integers in each test case. It takes no parameters and returns no value, but instead prints the results directly to stdout. The function assumes that the input is well-formed and does not perform any error checking.

