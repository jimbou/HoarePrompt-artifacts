#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    return int(sys.stdin.buffer.readline())
    #The program returns an integer that is greater than 0

#Overall this is what the function does:Reads an integer from standard input and returns it, ensuring the returned value is greater than 0.

#State of the program right berfore the function call: stdin contains a line with two space-separated integers n and k, where n and k are positive integers and 1 <= k <= n <= 10^6.
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing two positive integers n and k, where n is between 1 and 10^6 (inclusive) and k is between 1 and n (inclusive), and these integers are read from the standard input as space-separated values.

#Overall this is what the function does:Reads two positive integers n and k from the standard input, where n is between 1 and 10^6 (inclusive) and k is between 1 and n (inclusive), and returns them as a map object.

#State of the program right berfore the function call: stdin contains a line with two space-separated integers n and k, where n and k are positive integers such that 2 <= n <= 10^6 and 1 <= k <= n.
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of two integers, where the first integer is n and the second integer is k, both of which are positive integers such that 2 <= n <= 10^6 and 1 <= k <= n.

#Overall this is what the function does:Reads a line from standard input, splits it into two space-separated integers, and returns them as a list of two positive integers, where the first integer is n and the second integer is k, such that 2 <= n <= 10^6 and 1 <= k <= n.

#State of the program right berfore the function call: rows_number is a positive integer
    return [func_3() for _ in range(rows_number)]
    #The program returns a list of 'rows_number' number of elements, where each element is the result of calling the function 'func_3()'. The exact value of each element is unknown since the definition of 'func_3()' is not provided, but it is known that 'rows_number' is a positive integer.

#Overall this is what the function does:This function generates a list of elements by repeatedly calling the 'func_3()' function a specified number of times, equal to the value of the 'rows_number' parameter, and returns the resulting list. The function does not modify the input 'rows_number' parameter. The exact values of the elements in the returned list are determined by the 'func_3()' function, which is not defined in the provided code.

#State of the program right berfore the function call: stdin contains a sequence of bytes representing a string that ends with a newline character or an empty string.
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a string that is read from the standard input (stdin), with the trailing newline character removed, or an empty string if stdin is empty.

#Overall this is what the function does:Reads a line of input from the standard input (stdin), removes the trailing newline character if present, and returns the resulting string. If the standard input is empty, returns an empty string.

#State of the program right berfore the function call: stdin contains one input: a string
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns the input string from stdin, which is a single string input.

#Overall this is what the function does:Reads a single string input from standard input (stdin) and returns it as a decoded string, stripped of any trailing newline characters.

#State of the program right berfore the function call: stdin contains a single line with two space-separated integers.
    return [int(i) for i in input().split()]
    #The program returns a list of two integers that were input from stdin, each integer is a space-separated value from the single line of input.

#Overall this is what the function does:The function reads a single line of input from stdin, splits it into two space-separated integers, and returns them as a list of two integers.

#State of the program right berfore the function call: rows is a non-negative integer
    return [func_7() for _ in range(rows)]
    #The program returns a list of 'rows' number of elements, where each element is the return value of the function func_7(). The length of the list is equal to the value of 'rows', which is a non-negative integer.

#Overall this is what the function does:The function generates a list of a specified length, where each element is the result of calling the function func_7(), and returns this list. The length of the returned list is equal to the input parameter 'rows', which must be a non-negative integer.

#State of the program right berfore the function call: stdin contains one input: a string
    return input()
    #The program returns a string that was provided as input from stdin.

#Overall this is what the function does:The function reads a string from standard input and returns it unchanged, effectively echoing the input string.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    return int(input())
    #The program returns an integer greater than 0 that was provided as input

#Overall this is what the function does:The function reads an integer greater than 0 from standard input and returns it as is, without any modifications or transformations.

#State of the program right berfore the function call: stdin contains a string of two space-separated integers.
    return input().split()
    #The program returns a list of two strings, each representing an integer, which are space-separated in the input string from stdin.

#Overall this is what the function does:The function reads a string of two space-separated integers from standard input and returns them as a list of two strings, without performing any validation or conversion on the input values.

#State of the program right berfore the function call: d is a dictionary where each key is an integer and each value is a list of integers, processing is a list of integers, da is an integer representing a key in d, and rank is a list of integers. The length of processing and rank are equal to the maximum key value in d.
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns integer 1.
    #State: *`d` is a dictionary where each key is an integer and each value is a list of integers, `processing` is a list of integers, `da` is an integer representing a key in `d`, `rank` is a list of integers, and `tmp` is an integer equal to 10^9. The length of `processing` and `rank` are equal to the maximum key value in `d`. The length of the list associated with the key `da` in `d` is more than 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: d is a dictionary where each key is an integer and each value is a list of integers, processing is a list of integers, da is an integer representing a key in d, rank is a list of integers, and tmp is an integer. The value of tmp is the minimum of its original value (10^9) and the return values of func_12(d, processing, di, rank) for all di in d[da] where processing[di - 1] is 0.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the minimum value of tmp (which is 10^9) and the return values of func_12(d, processing, di, rank) for all di in d[da] where processing[di - 1] is 0, plus 1.

#Overall this is what the function does:This function calculates a rank value based on a dictionary `d`, a list `processing`, an integer `da`, and a list `rank`. It returns an integer value representing the calculated rank. If the list associated with the key `da` in `d` has only one element, the function returns 1. Otherwise, it iterates over the elements in the list, updates the `processing` list, and recursively calls another function `func_12` to calculate a minimum value. The function then updates the `rank` list with this minimum value plus 1 and returns the same value.

#State of the program right berfore the function call: a and b are non-negative integers, a >= b.
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns a tuple containing the values of x, y, and a. x is 1, y is 0, and a is a non-negative integer.
    #State: a and b are non-negative integers, a >= b, and b is not equal to 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns a tuple containing three values: y, x - a // b * y, and g. Here, y, x, and g are the returned values from the function func_13(b, a % b). The value of x - a // b * y is calculated using the returned values of x and y, and the initial state values of a and b, where a and b are non-negative integers, b is not equal to 0, and a is greater than or equal to b.

#Overall this is what the function does:This function calculates and returns the greatest common divisor (GCD) of two non-negative integers, a and b, where a is greater than or equal to b. It also returns the coefficients x and y such that ax + by = gcd(a, b). If b is 0, the function returns (1, 0, a), indicating that the GCD is a and the coefficients are 1 and 0. Otherwise, it recursively calls another function, func_13, to calculate the GCD and coefficients, and then returns the calculated values.

#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
    n, k = func_7()
    b = bin(n)[2:]
    l = len(b)
    if (k == 1) :
        if (n == 2) :
            return '1\n2'
            #The program returns a string '1\n2'. The string '1' is a binary string of length 1, and the string '2' is a decimal number that is equal to the value of n. The value of n is 2, and k is equal to 1. The length of the binary string b is equal to the number of bits in the binary representation of n, which is 1.
        #State: *n and k are integers such that 1 <= k <= n <= 10^6, k is equal to 1, b is a binary string of length l, l is an integer equal to the number of bits in the binary representation of n, and n is not equal to 2
    else :
        bk = bin(k)[2:]
        ans = []
        lk = len(bk)
        for i in range(lk - 1):
            ans.append(2 ** i)
            
        #State: `n` is an integer such that 1 <= k <= n <= 10^6, `k` is an integer such that 1 <= k <= n <= 10^6 and `k` is not equal to 1, `b` is a binary string of length `l`, `l` is an integer equal to the number of bits in the binary representation of `n`, `bk` is a binary string equal to the binary representation of `k`, `ans` is a list containing the integers 1, 2, 4, ..., 2^(lk-2), `lk` is an integer equal to the length of `bk` and must be at least 2, `i` is lk-2.
        ans.append(k - 1 - sum(ans))
        ans.append(k + 1)
        ans.append(2 * k + 1)
        for i in range(lk, l):
            ans.append(2 ** i)
            
        #State: n is an integer such that 1 <= k <= n <= 10^6, k is an integer such that 1 <= k <= n <= 10^6 and k is not equal to 1, b is a binary string of length l, l is an integer equal to the number of bits in the binary representation of n, bk is a binary string equal to the binary representation of k, lk is an integer equal to the length of bk and must be at least 2 and less than l, i is equal to l, ans is a list containing the integers 1, 2, 4, ..., 2^(lk-2), k - 1 - sum(ans), k + 1, 2 * k + 1, 2^lk, 2^(lk+1), ..., 2^(l-1).
    #State: *n and k are integers such that 1 <= k <= n <= 10^6, b is a binary string of length l, l is an integer equal to the number of bits in the binary representation of n. If k is equal to 1 and n is not equal to 2, the program executes the if part. Otherwise, k is an integer such that 1 <= k <= n <= 10^6 and k is not equal to 1, b is a binary string of length l, lk is an integer equal to the length of the binary representation of k and must be at least 2 and less than l, i is equal to l, ans is a list containing the integers 1, 2, 4, ..., 2^(lk-2), k - 1 - sum(ans), k + 1, 2 * k + 1, 2^lk, 2^(lk+1), ..., 2^(l-1).
    return str(len(ans)) + '\n' + ' '.join(map(str, ans))
    #The program returns a string that contains the length of the list 'ans' and the elements of the list 'ans'. The length of 'ans' is equal to the number of elements in the list, which is 2^(lk-2) + 5, where lk is the length of the binary representation of k. The elements of 'ans' are the integers 1, 2, 4, ..., 2^(lk-2), k - 1 - sum(ans), k + 1, 2 * k + 1, 2^lk, 2^(lk+1), ..., 2^(l-1), where l is the length of the binary representation of n.

#Overall this is what the function does:This function generates a list of integers based on the binary representation of input integers n and k, and returns a string containing the length of the list and its elements. If k is 1 and n is 2, it returns a specific string '1\n2'. Otherwise, it constructs the list by appending powers of 2, k-related values, and additional powers of 2, and returns the list's length and elements as a string.

#State of the program right berfore the function call: The function func_10() returns a non-negative integer, and the functions func_14() returns a value that can be converted to a string.
    for _ in range(func_10()):
        sys.stdout.write(str(func_14()) + '\n')
        
    #State: The loop has finished executing, and the standard output has been updated with the string representation of the value returned by `func_14()` followed by a newline character, for a total of `func_10()` iterations.

#Overall this is what the function does:The function writes the string representation of the value returned by `func_14()` followed by a newline character to the standard output, repeating this process a number of times equal to the non-negative integer returned by `func_10()`.

