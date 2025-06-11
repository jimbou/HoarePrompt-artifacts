#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines each containing an integer x (2 <= x <= 1000).
    num = int(input('Enter number of entries- '))
    L1 = []
    res = []
    for i in range(num):
        L1.append(int(input('Enter entry no.' + str(i + 1) + '- ')))
        
    #State: `num` is an integer between 1 and 1000, `L1` is a list containing `num` integers between 2 and 1000, `res` is an empty list, `stdin` contains 0 lines, `i` is `num-1`, `num` must be greater than or equal to 0
    for i in range(num):
        for j in range(2, L1[i] + 1):
            if L1[i] % j == 0:
                res.append(L1[i] // j * (j - 1))
                break
        
    #State: num is an integer between 0 and 1000, L1 is a list containing num integers between 2 and 1000, res is a list containing num integers plus L1[i] // j * (j - 1) if L1[i] is divisible by j, otherwise res is a list containing num integers, stdin contains 0 lines, i is equal to num.
    print(*res, sep='\n')
    #This is printed: the elements of the list res, separated by newline characters (where res is a list containing num integers plus L1[i] // j * (j - 1) if L1[i] is divisible by j, otherwise res is a list containing num integers)

#Overall this is what the function does:This function reads a number of entries from the user, then for each entry, it reads an integer and calculates the product of the integer divided by its smallest divisor (greater than 1) and the divisor minus 1. The results are then printed out, one per line. If an entry is a prime number (i.e., it has no divisors other than 1 and itself), the function will not calculate a result for that entry and will not print anything for it.

