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
        
    #State: Output State: The output state after the loop executes all the iterations is that the standard output contains `numCases` number of integers, each representing the sum of the minimum of each pair of integers in the corresponding test case. The value of `numCases` remains unchanged, and the standard input is empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by 2n integers. It then sorts the integers in ascending order, pairs them up, and calculates the sum of the minimum value in each pair. The function prints the sum for each test case, resulting in numCases number of integers being output to standard output. The function does not modify the input values or store any results internally, and it does not perform any actions other than reading input, processing the data, and printing the output.

