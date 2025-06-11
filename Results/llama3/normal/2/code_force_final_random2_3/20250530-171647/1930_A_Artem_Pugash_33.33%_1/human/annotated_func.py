#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by 2n integers a_1,a_2,...,a_{2n} (1 <= a_i <= 10^7).
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
        
    #State: numCases is 0, i is numCases, stdin contains 0 test cases, numInteger is an integer between 1 and 50, inclusive, numbers is an empty list, suma is the sum of the minimum of all pairs of adjacent elements in the original numbers list, and the sum of the minimum of all pairs of adjacent elements in the original numbers list which is suma is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by 2n integers. It sorts the integers in ascending order, pairs them up, and calculates the sum of the minimum value in each pair. The function then prints the sum for each test case. The function does not return any value, but rather prints the results directly to the console.

