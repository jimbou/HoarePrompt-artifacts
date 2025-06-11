#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    return int(sys.stdin.buffer.readline())
    #The program returns an integer greater than 0 that was provided as input through stdin.

#Overall this is what the function does:Reads an integer greater than 0 from standard input and returns it.

#State of the program right berfore the function call: stdin contains a line with two space-separated integers. The first integer is a positive integer and the second integer is a positive integer less than or equal to the first integer.
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing two integers, where the first integer is a positive integer and the second integer is a positive integer less than or equal to the first integer.

#Overall this is what the function does:Reads a line from standard input, splits it into two space-separated integers, and returns a map object containing these two integers, where the first integer is positive and the second integer is positive and less than or equal to the first integer.

#State of the program right berfore the function call: stdin contains a line with two space-separated integers. The first integer is a positive integer and the second integer is a positive integer less than or equal to the first integer.
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of two integers, where the first integer is a positive integer and the second integer is a positive integer less than or equal to the first integer.

#Overall this is what the function does:Reads a line from standard input, splits it into two space-separated integers, and returns them as a list, where the first integer is a positive integer and the second integer is a positive integer less than or equal to the first integer.

#State of the program right berfore the function call: rows_number is a positive integer
    return [func_3() for _ in range(rows_number)]
    #The program returns a list containing the result of func_3() repeated rows_number times, where rows_number is a positive integer and the value of func_3() is unknown.

#Overall this is what the function does:The function generates a list containing the result of func_3() repeated a specified number of times, where the specified number is a positive integer, and returns this list. The value of func_3() is unknown.

#State of the program right berfore the function call: stdin is a file-like object containing a sequence of bytes that can be read and decoded into a string. The string represents a line of input from the standard input, terminated by a newline character or the end of the file.
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a bytes object representing a line of input from the standard input, with the trailing newline character or other trailing bytes removed.

#Overall this is what the function does:Reads a line of input from the standard input and returns it as a bytes object with trailing newline character or other trailing bytes removed.

#State of the program right berfore the function call: stdin is a file-like object that contains a string ending with a newline character.
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string that was read from the file-like object stdin, with the trailing newline character removed and decoded into a string.

#Overall this is what the function does:Reads a line of input from the standard input (stdin), removes the trailing newline character, and returns the resulting string.

#State of the program right berfore the function call: stdin contains one input: a space-separated list of two integers.
    return [int(i) for i in input().split()]
    #The program returns a list of two integers that were provided as input in stdin, separated by a space.

#Overall this is what the function does:Reads a space-separated list of two integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: rows is a positive integer
    return [func_7() for _ in range(rows)]
    #The program returns a list of 'rows' number of elements, where each element is the return value of the function 'func_7()'. The exact value of each element is unknown since the implementation of 'func_7()' is not provided, but it is known that 'rows' is a positive integer, so the list will have at least one element.

#Overall this is what the function does:The function generates a list of a specified number of elements, where each element is the result of calling the function 'func_7()'. The list will have at least one element, as the number of elements is determined by the positive integer 'rows'. The exact values of the elements are unknown, as they depend on the implementation of 'func_7()'.

#State of the program right berfore the function call: stdin contains one input: a string
    return input()
    #The program returns the input string that was provided through stdin.

#Overall this is what the function does:The function reads a string from standard input and returns it without any modifications.

#State of the program right berfore the function call: stdin contains one input: an integer.
    return int(input())
    #The program returns an integer that was provided as input from stdin.

#Overall this is what the function does:The function reads an integer from standard input and returns it without modification.

#State of the program right berfore the function call: stdin contains a string of space-separated values
    return input().split()
    #The program returns a list of strings where each string is a space-separated value from the input string in stdin.

#Overall this is what the function does:The function reads a string of space-separated values from standard input and returns a list of strings, where each string is a value from the input string.

#State of the program right berfore the function call: d is a dictionary where each key is an integer and each value is a list of integers, processing is a list of integers, da is an integer representing a key in dictionary d, and rank is a list of integers.
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns the integer 1.
    #State: *`d` is a dictionary where each key is an integer and each value is a list of integers, `processing` is a list of integers, `da` is an integer representing a key in dictionary `d`, `rank` is a list of integers, and `tmp` is 1000000000. The length of the list associated with key `da` in dictionary `d` is not equal to 1
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: The output state is the same as the initial state, except that the value of `tmp` may have changed. The value of `tmp` is now the minimum of its initial value (1000000000) and the minimum value returned by `func_12(d, processing, di, rank)` for each `di` in `d[da]` where `processing[di - 1]` is 0. The values of `d`, `processing`, `da`, and `rank` remain unchanged.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the minimum value between 1000000000 and the minimum value returned by `func_12(d, processing, di, rank)` for each `di` in `d[da]` where `processing[di - 1]` is 0, plus 1.

#Overall this is what the function does:This function calculates and returns the minimum rank of a given key (`da`) in a dictionary (`d`) based on the values associated with that key and the results of recursive calls to `func_12`. If the key has only one associated value, it returns 1. Otherwise, it iterates through the associated values, temporarily marking them as processed, and recursively calls `func_12` to calculate their ranks. The function returns the minimum rank found, plus 1, and updates the `rank` list with this value. The function does not modify the original dictionary (`d`) or the `processing` list.

#State of the program right berfore the function call: a and b are integers and b is non-zero.
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns a tuple containing the values of x, y, and a. The value of x is 1, the value of y is 0, and the value of a is an integer.
    #State: *a and b are integers and b is non-zero
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns a tuple containing three values: y, x - a // b * y, and g. y is the second return value of func_13(b, a % b), x is the first return value of func_13(b, a % b), a // b is the integer division of a by b, and g is the third return value of func_13(b, a % b).

#Overall this is what the function does:This function performs the Extended Euclidean Algorithm, which calculates the greatest common divisor (GCD) of two integers 'a' and 'b', and returns the GCD along with the coefficients of Bézout's identity. If 'b' is zero, it returns a tuple containing 1, 0, and 'a'. Otherwise, it recursively calls another function 'func_13' with 'b' and the remainder of 'a' divided by 'b', and returns the results along with the calculated coefficients. The function ultimately returns a tuple containing the GCD and the coefficients of Bézout's identity, which can be used to express the GCD as a linear combination of 'a' and 'b'.

#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
    n, k = func_7()
    b = bin(n)[2:]
    l = len(b)
    if (k == 1) :
        if (n == 2) :
            return '1\n2'
            #The program returns a string '1\n2' where '1' is a string of one character and '2' is a string of one character.
        #State: *n and k are integers such that 1 <= k <= n, k is currently equal to 1, b is a string of binary digits, l is an integer equal to the number of digits in b, and n is not equal to 2
    else :
        bk = bin(k)[2:]
        ans = []
        lk = len(bk)
        for i in range(lk - 1):
            ans.append(2 ** i)
            
        #State: Output State: n is an integer, k is an integer larger than 1, b is a string of binary digits, l is an integer equal to the number of digits in b, bk is a string of binary digits representing the value of k, ans is a list of integers [1, 2, 4, 8, ... , 2^(lk-2)], lk is an integer equal to the number of digits in bk.
        ans.append(k - 1 - sum(ans))
        ans.append(k + 1)
        ans.append(2 * k + 1)
        for i in range(lk, l):
            ans.append(2 ** i)
            
        #State: Output State: n is an integer, k is an integer larger than 1, b is a string of binary digits, l is an integer equal to the number of digits in b, bk is a string of binary digits representing the value of k, lk is an integer equal to the number of digits in bk, ans is a list of integers [1, 2, 4, 8, ..., 2^(lk-2), k - 2^(lk-1), k + 1, 2 * k + 1, 2^lk, 2^(lk+1), ..., 2^(l-1)].
    #State: *n and k are integers such that 1 <= k <= n, b is a string of binary digits, l is an integer equal to the number of digits in b. If k is equal to 1 and n is not equal to 2, then the state of the variables remains unchanged. If k is larger than 1, then the output state is as follows: n is an integer, k is an integer larger than 1, b is a string of binary digits, l is an integer equal to the number of digits in b, bk is a string of binary digits representing the value of k, lk is an integer equal to the number of digits in bk, ans is a list of integers [1, 2, 4, 8, ..., 2^(lk-2), k - 2^(lk-1), k + 1, 2 * k + 1, 2^lk, 2^(lk+1), ..., 2^(l-1)].
    return str(len(ans)) + '\n' + ' '.join(map(str, ans))
    #The program returns a string that contains the length of list 'ans' and the elements of list 'ans'. The length of list 'ans' is an integer. The elements of list 'ans' are integers that include 1, 2, 4, 8, ..., 2^(lk-2), k - 2^(lk-1), k + 1, 2 * k + 1, 2^lk, 2^(lk+1), ..., 2^(l-1). The variable 'lk' is an integer equal to the number of digits in the binary representation of 'k'. The variable 'l' is an integer equal to the number of digits in string 'b'.

#Overall this is what the function does:This function generates a sequence of integers based on the input parameters n and k. If k is 1 and n is 2, it returns the string '1\n2'. Otherwise, it constructs a list of integers that includes powers of 2 up to the number of digits in the binary representation of k, followed by k-1 minus the sum of the previous powers of 2, k+1, 2k+1, and then the remaining powers of 2 up to the number of digits in the binary representation of n. The function returns a string containing the length of this list and the list elements themselves.

#State of the program right berfore the function call: The function func_10() returns a non-negative integer, and the function func_14() returns a string.
    for _ in range(func_10()):
        sys.stdout.write(str(func_14()) + '\n')
        
    #State: Output State: The function func_10() returns a non-negative integer, and the function func_14() returns a string. The loop iterates func_10() times, writing the string returned by func_14() followed by a newline character to the standard output each time.

#Overall this is what the function does:This function writes a string returned by func_14() to the standard output a number of times equal to the non-negative integer returned by func_10(), with each string followed by a newline character.

