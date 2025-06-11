#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a list of integers (the length of the permutation p for each test case). Each integer in the list is in the range [3, 10^5] and the sum of these integers does not exceed 10^5.
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
    #This is printed: the elements of list a (where a is a list of integers from 1 to the number of test cases, with every other element reversed)

#Overall this is what the function does:The function reads an integer from standard input, representing the number of test cases, and then reads a list of integers representing the length of permutations for each test case. It generates a list of integers from 1 to the number of test cases, reverses every other element in the list, and prints the modified list.

