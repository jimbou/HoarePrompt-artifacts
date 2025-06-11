#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 5000) followed by t test cases. Each test case contains an integer n (1 ≤ n ≤ 50) followed by 2n integers a_1,a_2,…,a_{2n} (1 ≤ a_i ≤ 10^7).
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
        
    #State: numCases is 0, i is the original value of numCases minus 1, stdin contains 0 test cases, numInteger is an integer between 1 and 50 (inclusive), numbers is an empty list, and suma is the original value of suma plus the sum of the minimum of each pair of integers in the original list of numbers, repeated numCases times.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by 2n integers. It then sorts the integers in ascending order, pairs them up, and calculates the sum of the minimum value in each pair. The function prints the sum for each test case and repeats this process for the specified number of test cases.

