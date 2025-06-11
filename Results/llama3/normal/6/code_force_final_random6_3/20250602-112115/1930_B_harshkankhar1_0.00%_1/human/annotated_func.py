#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then for each test case, an integer (the length of the permutation, which is greater than or equal to 3 and less than or equal to 10^5).
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: a list of integers from 1 to the input integer, with every other element reversed

#Overall this is what the function does:Reverses every other element in a list of integers from 1 to a given input integer, starting from the first element, and prints the modified list.

