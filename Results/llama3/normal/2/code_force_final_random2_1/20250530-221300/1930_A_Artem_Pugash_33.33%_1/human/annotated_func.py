#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 ≤ n ≤ 50). The second line contains 2n integers a_1,a_2,...,a_{2n} (1 ≤ a_i ≤ 10^7).
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
        
    #State: numCases is an integer between 1 and 50, i is equal to numCases - 1, numInteger is an integer between 1 and 50, numbers is an empty list, stdin contains no test cases, a is an integer equal to the last number in the original list, b is an integer equal to the second last number in the original list, and the sum of the minimum of each pair of adjacent numbers in the original list, which is equal to suma, is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by 2n integers. It then sorts the integers in ascending order, pairs them up, and calculates the sum of the minimum value in each pair. Finally, it prints the sum for each test case. The function does not return any value, but rather prints the results directly to the console.

