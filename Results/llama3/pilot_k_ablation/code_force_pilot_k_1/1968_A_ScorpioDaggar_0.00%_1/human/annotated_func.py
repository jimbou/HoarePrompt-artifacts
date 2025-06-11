#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a series of integers (the test cases), each integer is greater than 1.
    num = int(input('Enter number of entries- '))
    L1 = []
    res = []
    for i in range(num):
        L1.append(int(input('Enter entry no.' + str(i + 1) + '- ')))
        
    #State: `num` is an integer, `L1` is a list containing `num` integers, `res` is an empty list, stdin contains a series of integers representing the test cases minus `num` integers.
    for i in range(num):
        for j in range(2, L1[i] + 1):
            if L1[i] % j == 0:
                res.append(L1[i] // j * (j - 1))
                break
        
    #State: num is an integer, L1 is a list containing num integers, res is a list containing num integer elements where each element is the product of the smallest divisor of the corresponding element in L1 minus one and the corresponding element in L1 divided by the smallest divisor, stdin contains a series of integers representing the test cases minus num integers.
    print(*res, sep='\n')
    #This is printed: the product of the smallest divisor of each element in L1 minus one and the corresponding element in L1 divided by the smallest divisor (where the elements are from the list res)

#Overall this is what the function does:This function reads a series of integers from standard input, calculates the product of the smallest divisor of each integer minus one and the integer divided by the smallest divisor, and prints these products to standard output.

