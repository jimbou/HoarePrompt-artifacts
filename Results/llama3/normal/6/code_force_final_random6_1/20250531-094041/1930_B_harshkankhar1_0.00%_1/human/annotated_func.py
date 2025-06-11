#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a series of integers (the length of the permutation p for each test case). Each integer is greater than or equal to 3 and less than or equal to 10^5. The sum of all integers does not exceed 10^5.
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: a list of integers from 1 to the input integer, with every other element reversed

#Overall this is what the function does:The function reads an integer from standard input, generates a list of integers from 1 to the input integer, reverses every other element in the list, and prints the modified list.

