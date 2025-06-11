#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    return int(sys.stdin.buffer.readline())
    #The program returns an integer greater than 0 that was provided as input through stdin.

#Overall this is what the function does:Reads an integer greater than 0 from standard input and returns it.

#State of the program right berfore the function call: stdin contains a line with two space-separated integers. The first integer is a positive integer (number of test cases) and the second integer is a positive integer (number of elements in the sequence).
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing two integers. The first integer is a positive integer representing the number of test cases, and the second integer is a positive integer representing the number of elements in the sequence.

#Overall this is what the function does:Reads a line from standard input, splits it into two space-separated integers, and returns a map object containing these integers, where the first integer represents the number of test cases and the second integer represents the number of elements in a sequence.

#State of the program right berfore the function call: stdin contains a line with two space-separated integers. The first integer is a positive integer and the second integer is a positive integer.
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of two integers. The first integer is a positive integer and the second integer is a positive integer.

#Overall this is what the function does:Reads a line from standard input, splits it into two space-separated integers, and returns them as a list of two positive integers.

#State of the program right berfore the function call: rows_number is a positive integer.
    return [func_3() for _ in range(rows_number)]
    #The program returns a list of 'rows_number' number of elements, where each element is the result of the function 'func_3()'. The exact values of the elements in the list are unknown since the definition of 'func_3()' is not provided, but it is known that the list will have 'rows_number' number of elements, where 'rows_number' is a positive integer.

#Overall this is what the function does:Generates a list of 'rows_number' elements, where each element is the result of calling 'func_3()', and returns this list. The length of the returned list is equal to the input 'rows_number', which is a positive integer.

#State of the program right berfore the function call: stdin is a file object connected to a valid input source, and the next line of input is a string that can be read without errors.
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a string that is the next line of input from the valid input source connected to stdin, with trailing newlines removed.

#Overall this is what the function does:Reads the next line of input from a valid input source connected to stdin, removes trailing newlines, and returns the resulting string.

#State of the program right berfore the function call: stdin is a file-like object that contains a single line of input, which is a string that can be decoded using the UTF-8 encoding scheme.
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string that was read from the file-like object stdin, which is decoded using the UTF-8 encoding scheme and has its trailing newline character removed.

#Overall this is what the function does:Reads a single line of input from the standard input (stdin), decodes it using UTF-8 encoding, removes the trailing newline character, and returns the resulting string.

#State of the program right berfore the function call: stdin contains a line with two space-separated integers.
    return [int(i) for i in input().split()]
    #The program returns a list of two integers that were read from the input line.

#Overall this is what the function does:Reads a line from standard input, splits it into two space-separated integers, and returns them as a list of two integers.

#State of the program right berfore the function call: rows is a positive integer
    return [func_7() for _ in range(rows)]
    #The program returns a list of 'rows' number of elements, where each element is the return value of the function 'func_7()'. The exact value of each element is unknown since the implementation of 'func_7()' is not provided, but it is known that 'rows' is a positive integer, so the list will have at least one element.

#Overall this is what the function does:This function generates a list of a specified number of elements, where each element is the result of calling the function 'func_7()'. The function takes one parameter, 'rows', which is a positive integer, and returns a list with 'rows' number of elements. The exact values of the elements in the list are determined by the implementation of 'func_7()', but the list will always have at least one element.

#State of the program right berfore the function call: stdin contains one input: a string
    return input()
    #The program returns a string that was provided as input from stdin.

#Overall this is what the function does:Reads a string from standard input and returns it unchanged.

#State of the program right berfore the function call: stdin contains one input: an integer.
    return int(input())
    #The program returns an integer that was provided as input from stdin.

#Overall this is what the function does:Reads an integer from standard input and returns it as an integer value.

#State of the program right berfore the function call: stdin contains a string of two space-separated integers.
    return input().split()
    #The program returns a list of two integers that were originally space-separated in the input string from stdin.

#Overall this is what the function does:The function reads a string of two space-separated integers from standard input, splits the string into two integers, and returns them as a list.

#State of the program right berfore the function call: d is a dictionary where each key is an integer and each value is a list of integers, processing is a list of integers of the same length as the number of keys in d, da is an integer representing a key in d, and rank is a list of integers of the same length as the number of keys in d.
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns the integer 1.
    #State: *`d` is a dictionary where each key is an integer and each value is a list of integers, `processing` is a list of integers of the same length as the number of keys in `d`, `da` is an integer representing a key in `d`, `rank` is a list of integers of the same length as the number of keys in `d`, and `tmp` is an integer equal to 10^9. The length of the list associated with the key `da` in `d` is more than 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: d is a dictionary where each key is an integer and each value is a list of integers, processing is a list of integers of the same length as the number of keys in d, da is an integer representing a key in d, rank is a list of integers of the same length as the number of keys in d, tmp is an integer equal to the minimum of its original value (10^9) and the return values of func_12(d, processing, di, rank) for all di in d[da] where processing[di - 1] is 0, and d[da] is a list of integers with a length equal to the number of iterations of the loop.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns tmp + 1, where tmp is the minimum of its original value (10^9) and the return values of func_12(d, processing, di, rank) for all di in d[da] where processing[di - 1] is 0, and rank[da - 1] is tmp + 1.

#Overall this is what the function does:This function calculates and returns the minimum rank of a given key `da` in a dictionary `d`, where the rank is determined by recursively exploring the values associated with `da` and updating the `rank` list accordingly. If the list associated with `da` has only one element, the function returns 1. Otherwise, it iterates through the list, temporarily marking each element as processed, and recursively calls `func_12` to calculate the minimum rank. The function then updates the `rank` list with the calculated minimum rank plus one and returns this value.

#State of the program right berfore the function call: a and b are integers such that b != 0 and a >= b >= 0.
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns a tuple containing three values: x which is 1, y which is 0, and a which is an integer greater than or equal to 0.
    #State: a and b are integers, a >= b, b is larger than 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns three values: y, x - a // b * y, and g. y is the second returned value of func_13(b, a % b), where a % b is the remainder of a divided by b. x - a // b * y is the first returned value of func_13(b, a % b) minus the product of the integer division of a by b and y. g is the third returned value of func_13(b, a % b).

#Overall this is what the function does:This function takes two integers, a and b, as input, where b is non-zero and a is greater than or equal to b, which is greater than or equal to 0. It returns a tuple of three values. If b is zero, the function returns 1, 0, and the original value of a. Otherwise, it recursively calls another function, func_13, with b and the remainder of a divided by b as arguments, and returns the second value of func_13, the first value of func_13 minus the product of the integer division of a by b and the second value of func_13, and the third value of func_13.

#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
    n, k = func_7()
    b = bin(n)[2:]
    l = len(b)
    if (k == 1) :
        if (n == 2) :
            return '1\n2'
            #The program returns a string '1\n2' where '1' is a string of a single digit that is equal to the current value of k, and '2' is a string of a single digit that is equal to the current value of n.
        #State: *n and k are integers such that 1 <= k <= n <= 10^6, k is currently equal to 1, b is a string of binary digits, l is an integer representing the length of b, and n is not equal to 2
    else :
        bk = bin(k)[2:]
        ans = []
        lk = len(bk)
        for i in range(lk - 1):
            ans.append(2 ** i)
            
        #State: `n` is an integer such that 1 <= k <= n <= 10^6, `k` is an integer such that 1 <= k <= n <= 10^6 and `k` is not equal to 1, `b` is a string of binary digits, `l` is an integer representing the length of `b`, `bk` is a string of binary digits representing the binary value of `k`, `ans` is a list containing 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, `lk` is an integer representing the length of `bk` and `lk` is at least 21, `i` is 20
        ans.append(k - 1 - sum(ans))
        ans.append(k + 1)
        ans.append(2 * k + 1)
        for i in range(lk, l):
            ans.append(2 ** i)
            
        #State: Output State: `n` is an integer such that 1 <= k <= n <= 10^6, `k` is an integer such that 1 <= k <= n <= 10^6 and k is not equal to 1, `b` is a string of binary digits, `l` is an integer representing the length of b and l is greater than lk, `bk` is a string of binary digits representing the binary value of k, `ans` is a list containing 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, k - 1 - sum(ans), k + 1, 2 * k + 1, 2^lk, 2^(lk + 1), 2^(lk + 2), ..., 2^(l - 1), `lk` is an integer representing the length of bk and lk is at least 21, `i` is l
        #
        #The output state after the loop executes all the iterations is that the list `ans` will contain all the powers of 2 from 2^lk to 2^(l - 1), and the variable `i` will be equal to `l`. The other variables remain unchanged.
    #State: *n and k are integers such that 1 <= k <= n <= 10^6, b is a string of binary digits, l is an integer representing the length of b. If k is equal to 1, n is not equal to 2. If k is not equal to 1, the list `ans` contains all the powers of 2 from 2^lk to 2^(l - 1), where lk is the length of the binary representation of k and is at least 21, and the variable `i` is equal to `l`.
    return ' '.join(map(str, ans))
    #The program returns a string of space-separated powers of 2, starting from 2^lk to 2^(l - 1), where lk is the length of the binary representation of k and is at least 21, and l is the length of the binary string b. The powers of 2 are converted to strings before being joined by spaces.

#Overall this is what the function does:This function generates a string of space-separated powers of 2. If the input integer k is 1 and n is not 2, it returns the string '1\n2'. Otherwise, it calculates the powers of 2 from 2^lk to 2^(l - 1), where lk is the length of the binary representation of k and is at least 21, and l is the length of the binary string b. The function then returns a string of these powers of 2, converted to strings and joined by spaces.

#State of the program right berfore the function call: The function func_10() returns a non-negative integer and the function func_14() returns a non-negative integer.
    for _ in range(func_10()):
        sys.stdout.write(str(func_14()) + '\n')
        
    #State: The output of `func_14()`, a non-negative integer, is printed to the console followed by a newline character, `func_10()` returns a non-negative integer greater than or equal to the number of iterations, and `func_14()` returns a non-negative integer.

#Overall this is what the function does:Prints a non-negative integer to the console a certain number of times, where the integer is determined by `func_14()` and the number of times is determined by `func_10()`. The output is followed by a newline character. The function does not return any value.

